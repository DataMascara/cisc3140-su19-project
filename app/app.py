from flask import Flask, render_template, request, redirect, url_for, session
import requests
import json
import urllib.request
import webbrowser

# Relative path to reach the templates folder
app = Flask(__name__, template_folder="templates")
##Regen secret before production level
app.secret_key = "test"

# Assuming the API is running at the local ip below
api = "https://bc-api-class.herokuapp.com/"

@app.route("/", methods=["GET"])
def redirect_home():
    if "loggedin" in session:
        return redirect("/home/")
    return redirect("/login/")


"""
-------------LOGIN-------------
"""
@app.route("/login/", methods=["POST", "GET"])
def login_api():
    # already logged in
    trending = trending_ports()["all_ports"]
    if "loggedin" in session:
        return redirect("/home/")
    else:
        if request.method == "POST":
            res = request.form
            print(res)
            # Grab the user and pw
            username = res["username"]
            password = res["password"]
            api_res = requests.post(
                f"{api}/login/", json={"username": username, "password": password}
            ).json()
            try:
                # Make sure there is a user before we do anything with sessions
                if api_res["user"]["username"]:
                    session["user"] = api_res["user"]
                    # Create session data, we can access this data in other routes
                    session["loggedin"] = True
                    # session['id'] = account['id']
                    session["username"] = username
                    session["user"] = api_res["user"]
                    session["subscriptions"] = requests.get(
                        f"{api}/ports-for-username/", json={"username": username}
                    ).json()["all_subscriptions for {data_value}"]
                    session["votes"] = requests.get(
                        f"{api}/votes-for-username/", json={"username": username}
                    ).json()["voted_data"]
                    return redirect("/home/")
                    return render_template(
                        "base.html", title="Logged In", user=session["user"]
                    )
                else:
                    session["votes"]
                    return render_template(
                        "base.html", title="", errLogIn=True, trendPorts=trending
                    )
            except:
                return render_template(
                    "base.html", title="", errLogIn=True, trendPorts=trending
                )
        else:
            return render_template(
                "base.html", title="Please Log in", trendPorts=trending
            )


"""
-------------LOG-OUT-------------
"""
@app.route("/logout/")
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    session.pop("user", None)
    session.pop("subscriptions", None)
    session.pop("votes", None)
    # Redirect to login page
    return redirect("/login/")

"""
-------------HOMEPAGE-------------
"""
@app.route("/home/", methods=["GET"])
def home():
    # Use the helper method to grab "tredning ports"
    trending = trending_ports()["all_ports"]
    port = requests.get(f"{api}/posts-by-portname/", json={"portname": "Main"}).json()
    if "loggedin" in session:

        update_vote_for_post(port)
        return render_template(
            "posts.html",
            name="Home",
            user=session["user"],
            trendPorts=trending,
            port=port,
            search="My First Search!",
        )
    else:
        return render_template(
            "posts.html",
            name="Log In",
            trendPorts=None,
            port=None,
            search="My First Search!",
        )
 
"""
-------------/PORT(aka subreddit)-------------
- Uses the url to decide what port the user wants to go to.
        - So, this should
"""
@app.route("/p/<portname>/", methods=["GET"])
def portpost(portname):
    port = requests.get(f"{api}/posts-by-portname/", json={"portname": portname}).json()
    print(type(port))
    trending = trending_ports()["all_ports"]
    if "loggedin" in session:
        update_vote_for_post(port)
        return render_template(
            "posts.html",
            name="p/" + portname,
            user=session["user"],
            trendPorts=trending,
            port=port,
            search="My First Search!",
        )
    else:
        return render_template(
            "posts.html",
            name="p/" + portname,
            trendPorts=trending,
            port=port,
            search="My First Search!",
        )

'''
--------POST HISTORY------
'''
# gets user's post history
@app.route("/u/<username>/posts/", methods=["GET"])
def my_posts(username):
    trending = trending_ports()["all_ports"]
    port = requests.get(f"{api}/my-posts/", json={"username": username}).json()
    if "loggedin" in session:
        update_vote_for_post(port)
        return render_template(
            "posts.html",
            name=username + "'s Post",
            user=session["user"],
            trendPorts=trending,
            port=port,
            search="My First Search!",
        )
        # return port
    else:
        return render_template(
            "posts.html",
            name=username + "'s Post",
            trendPorts=trending,
            port=port,
            search="My First Search!",
        )

"""
-------------SIGN-UP-------------
"""
@app.route("/signup/", methods=["POST", "GET"])
def sign_up():
    trending = trending_ports()["all_ports"]
    # if loggedin why you signing up
    if "loggedin" in session:
        return redirect("/home/")

    if request.method == "POST":
        # Grab the form
        res = request.form
        print(res)
        email = res["email"]
        username = res["username"]
        password = res["password"]
        first = res["first"]
        last = res["last"]
        # avatarurl = res['imageUpload']
        avatarurl = ""
        # currently signup page has no description box
        # description = res["description"]
        description = ""

        api_res = requests.post(
            f"{api}/signup/",
            json={
                "email": email,
                "password": password,
                "username": username,
                "first": first,
                "last": last,
                "avatarurl": avatarurl,
                "description": description,
            },
        ).json()
        try:
            # Try and get the new user, meaning they registered
            username = api_res["user"][0]["username"]
        except:
            # Otherwise, render an error
            return render_template(
                "register.html", errUsernameInUse=api_res["error"], trendPorts=trending
            )

        # if this line is successful then the user is created
        # Load uses helper method returns the dict of the user
        # representation for local storage
        session["user"] = load_user(username)
        session["loggedin"] = True
        # session['id'] = account['id']
        session["username"] = username
        redirect("/home/")
        return render_template(
            "base.html", name="Bla", user=session["user"], trendPorts=trending
        )
    else:
        return render_template("register.html", trendPorts=trending)

"""
-------------NEW POST-------------
"""
@app.route("/new-post/", methods=["GET", "POST"])
def post():
    trending = trending_ports()["all_ports"]
    # Make sure the user is logged in

    if "loggedin" in session:
        # If we are making a post

        if request.method == "POST":
            try:
                res = request.form
                title = res["title"]
                portname = res["portname"]
                text = res["text"]
                response = requests.post(
                    f"{api}/newpost/",
                    json={
                        "title": title,
                        "text": text,
                        "portname": portname,
                        "userId": session["user"]["userId"],
                        "username": session["username"],
                    },
                ).json()
                trending = trending_ports()["all_ports"]
                return render_template(
                    "postSubmitted.html",
                    user=session["user"],
                    name="What Name",
                    trendPorts=trending,
                )

            except:
                return render_template(
                    "writePost.html",
                    user=session["user"],
                    error="Invalid Post",
                    trendPorts=trending,
                )
        # If the post fails, try again
        else:
            return render_template(
                "writePost.html", user=session["user"], trendPorts=trending
            )

    else:
        return redirect("/login/")

"""
-------------USER SUBSCRIBED POSTS-------------
 - Given a user, return all the posts from the ports they are subscribed to
"""
@app.route("/subscribed-posts/", methods=["GET"])
def subscribedposts():
    if "loggedin" in session:
        trending = trending_ports()["all_ports"]
        post = requests.get(
            f"{api}/posts-from-subscribed-ports/",
            json={"username": session["username"]},
        ).json()
        update_vote_for_post(post)
        return render_template(
            "posts.html",
            name="Your feed",
            user=session["user"],
            trendPorts=trending,
            port=post,
            search="My First Search!",
        )

        return post
    else:
        return redirect("/login/")

'''
----VOTE ON POST----
'''
@app.route("/vote/", methods=["POST"])
def vote():
    if "loggedin" in session:
        res = request.form
        value = res["value"]
        postId = res["postId"]
        originalValue = res["originalValue"]
        # print(res)
        response = (
            requests.post(
                f"{api}/vote/",
                json={
                    "username": session["username"],
                    "value": value,
                    "postId": postId,
                    "originalValue": originalValue,
                },
            ).json()
        )["voted_data"]
        # print(response)
        session["votes"] = response
        return "UPDATED"
    else:
        return redirect("/login/")

"""
-------------PORT INDEX-------------
- Allows logged in users to brows ports
"""
@app.route("/portindex/", methods=["GET"])
def portindex():
    trending = trending_ports()["all_ports"]
    ports = requests.get(f"{api}/allports/").json()["all_ports"]

    if "loggedin" in session:
        subscribed_ports = requests.get(
            f"{api}/ports-for-username/", json={"username": session["username"]}
        ).json()["all_subscriptions for {data_value}"]

        # this will iterate through all the ports that existing
        for p in ports:
            # this will iterate through all the ports that the user is subscribed
            for sp in subscribed_ports:
                # if the ids match then the user is subscribed to the port so 'isSubscribed'
                #  will be set to True
                if p["id"] == sp["portId"]:
                    # "isSubscribed" notifies the html page what
                    # state the button should be in
                    p.update({"isSubscribed": True})
        return render_template(
            "portIndex.html",
            name="Port Index",
            user=session["user"],
            ports=ports,
            trendPorts=trending,
        )
    else:
        return render_template(
            "portIndex.html", name="Port Index", ports=ports, trendPorts=trending
        )


"""
-------------SUBSCRIBE TO PORT-------------
"""
@app.route("/subscribe/", methods=["POST"])
def subscribe():
    if "loggedin" in session:
        res = request.form
        portname = res["portname"]
        username = session["username"]
        # Either going be joined(you're subscribing) or Subscribed,
        # meaning you want to unsubscribe
        state = res["value"]

        # If you click on subscribe(you just joined the port),
        if state == "Joined":
            requests.post(
                f"{api}/subscribe-to-port/",
                json={"portname": portname, "username": username},
            )
        else:
            requests.post(
                f"{api}/unsubscribe-to-port/",
                json={"portname": portname, "username": username},
            )
        return res
    else:
        return redirect("/login/")

'''
--- POST ---
'''
@app.route("/post/<title>")
def post_by_title(title):
    if "loggedin" in session:
        post_title = title
    # If you click on subscribe(you just joined the port),
        try:
            post_dict = requests.get(
                f"{api}/post-by-title/",
                json={"title": title}).json() 
            print(post_dict)    
            return render_template('postDetails.html', user = session['user'], name = "Post", post=post_dict)
        except:
            return redirect('/home/')
    else:
        return redirect("/login/")



"""
 ------PROFILE-----
"""
@app.route("/profile/", methods=["GET", "POST"])
def profile():
    trending = trending_ports()["all_ports"]
    if "loggedin" in session:

        #if user update their profile
        #get the form from website, convert it to JSON
        #update the description and avaterURL that user entered.
        if request.method == "POST":
            form = request.form.to_dict()
            headers = {"Content-Type": "application/json"}

            data = json.dumps(
            { "username":session["user"]["username"],
             "field":"description",
              "value":form["descriptionTextArea"] })
            print(data)

            response = requests.put(api + "update/", data=data, headers = headers)
            print(response.content)

            data = json.dumps(
            { "username":session["user"]["username"],
             "field":"avatarUrl",
              "value":form["avatarURL"] })
            print(data)

            response = requests.put(api + "update/", data=data, headers = headers)
            print(response.content)

            #change the session's user info
            session["user"]["avatarUrl"] = form["avatarURL"]
            session["user"]["description"] = form["descriptionTextArea"]

        print("hello")
        return render_template(
            "userInfo.html",
            userProfile=True,
            user=session["user"],
            viewedUser=session["user"],
            trendPorts=trending,
        )
    else:
        return redirect("/login/")



"""
------UPDATE-----
"""
@app.route("/update/", methods=["GET", "POST"])
def update():
    if "loggedin" in session:

        form = request.form.to_dict()
        headers = {"Content-Type": "application/json"}

        if request.method == "POST":

            if "emailSetting" in form.keys():

                payload = json.dumps(
                    {
                        "username": session["user"]["username"],
                        "field": "email",
                        "value": form["emailSetting"],
                    }
                )

                response = requests.put(api + "update/", data=payload, headers=headers)
                print(response.content)

                #update session's user userInfo
                session["user"]["email"] = form["emailSetting"]

                return render_template(
                    "userInfo.html",
                    user=session["user"]["username"],
                    accountSettings=True,
                    emailAndPassword=True,
                )

            else:

                payload = json.dumps(
                    {
                        "username": session["user"]["username"],
                        "field": "password",
                        "value": form["passwordSetting"],
                    }
                )

                response = requests.put(api + "/update/", data=payload, headers=headers)
                print(response.content)

                #update session's user userInfo
                session["user"]["password"] = form["passwordSetting"]

                return render_template(
                    "userInfo.html",
                    user=session["user"]["username"],
                    accountSettings=True,
                    emailAndPassword=True,
                )

            return render_template(
                "userInfo.html",
                user=session["user"]["username"],
                accountSettings=True,
                emailAndPassword=True,
            )
        else:
            return render_template(
                "userInfo.html",
                user=session["user"]["username"],
                accountSettings=True,
                emailAndPassword=True,
            )
    else:
        return redirect("/login/")


"""
------OUR TEAM PAGE-----
"""
@app.route("/ourteam/")
def ourteam():
    trending = trending_ports()["all_ports"]
    if "loggedin" in session:
        return render_template(
            "genLinks.html", user=session["user"], about=True, trendPorts=trending
        )
    else:
        return render_template("genLinks.html", about=True, trendPorts=trending)


"""
------CONTCT PAGE-----
"""
@app.route("/contact/")
def contact():
    trending = trending_ports()["all_ports"]
    if "loggedin" in session:
        return render_template(
            "genLinks.html", user=session["user"], contact=True, trendPorts=trending
        )
    else:
        return render_template("genLinks.html", contact=True, trendPorts=trending)

"""
------TERMS PAGE-----
"""
@app.route("/terms/")
def terms():
    trending = trending_ports()["all_ports"]
    if "loggedin" in session:
        return render_template(
            "genLinks.html", user=session["user"], terms=True, trendPorts=trending
        )
    else:
        return render_template("genLinks.html", terms=True, trendPorts=trending)

"""
------NEWS FEED-----
"""
@app.route("/newsfeed/")
def hello9():
    trending = trending_ports()["all_ports"]
    return render_template(
        "posts.html",
        name="Bla",
        trendPorts=trending,
        port="Main",
        search="My First Search!",
    )


@app.route("/Regist_Pending/")
def pending():
    user = session["user"]
    trending = trending_ports()["all_ports"]
    return render_template(
        "genLinks.html", name=user["first"], user=user, trendPorts=trending
    )
# helper function to get "trending posts"
# WIll do this by just getting three three random ports
def trending_ports():
    ports = requests.get(f"{api}/allports/")
    # Add way of deciding what ports are "trending"
    # Return a dictonary of the port representation
    return ports.json()


def update_vote_for_post(port):
    if "loggedin" in session:
        for posts in port["posts"]:
            for votes in session["votes"]:
                if posts["postId"] == votes["postId"]:
                    print(votes["vote"])
                    posts.update({"upOrDownvoted": votes["vote"]})
        return port
    else:
        return None


        


def load_user(username):
    user = (requests.get(f"{api}/user", json={"username": username}).json())["user"][0]
    print(user)
    return user


if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)
