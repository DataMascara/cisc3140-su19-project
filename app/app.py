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
api = "https://bc-api-class.herokuapp.com"
# api = "http://127.0.0.1:5000"

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
    trending = trending_ports()
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
                    trending = trending_ports()
                    session.pop("trending", None)
                    trending = trending_ports()
                    return redirect("/home/")
                else:
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
    session.pop("trending", None)
    # Redirect to login page
    return redirect("/login/")

"""
-------------HOMEPAGE-------------
"""
@app.route("/home/", methods=["GET"])
def home():
    # Use the helper method to grab "tredning ports"
    trending = trending_ports()
    posts = requests.get(f"{api}/posts-by-portname/", json={"portname": "Main"}).json()
    # print(post)

    if "loggedin" in session:
        update_vote_for_post(posts)
        return render_template(
            "posts.html",
            name="Home",
            user=session["user"],
            trendPorts=trending,
            port=posts)
    else:
        return render_template(
            "posts.html",
            name="Log In",
            trendPorts=None,
            port=None
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
    trending = trending_ports()
    if "loggedin" in session:
        update_vote_for_post(port)
        return render_template(
            "posts.html",
            name="p/" + portname,
            user=session["user"],
            trendPorts=trending,
            port=port
        )
    else:
        return render_template(
            "posts.html",
            name="p/" + portname,
            trendPorts=trending,
            port=port
        )

'''
--------POST HISTORY------
'''
# gets user's post history
@app.route("/u/<username>/posts/", methods=["GET"])
def my_posts(username):
    trending = trending_ports()
    port = requests.get(f"{api}/my-posts/", json={"username": username}).json()
    if "loggedin" in session:
        update_vote_for_post(port)
        return render_template(
            "posts.html",
            name=username + "'s Post",
            user=session["user"],
            trendPorts=trending,
            port=port
        )
        # return port
    else:
        return render_template(
            "posts.html",
            name=username + "'s Post",
            trendPorts=trending,
            port=port
        )

"""
-------------SIGN-UP-------------
"""
@app.route("/signup/", methods=["POST", "GET"])
def sign_up():
    trending = trending_ports()
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
        try:
            avatarurl = res["addimage"]
        except:
            avatarurl = ' '
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
        session["subscriptions"] = requests.get(
            f"{api}/ports-for-username/", json={"username": username}
        ).json()["all_subscriptions for {data_value}"]
        session["votes"] = requests.get(
            f"{api}/votes-for-username/", json={"username": username}
        ).json()["voted_data"]
        session["user"]["avatarUrl"] = avatarurl
        print(session)
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
    trending = trending_ports()
    # Make sure the user is logged in

    if "loggedin" in session:
        # If we are making a post

        if request.method == "POST":
            try:
                res = request.form
                title = res["title"]
                portname = res["communitysearch"]
                text = res["text"]
                print(res)
                try:
                    img = res["addimage"]
                except:
                    img =  'https://media.wired.com/photos/5cdefc28b2569892c06b2ae4/master/w_1500,c_limit/Culture-Grumpy-Cat-487386121-2.jpg' 
                response = requests.post(
                    f"{api}/newpost/",
                    json={
                        "title": title,
                        "text": text,
                        "portname": portname,
                        "userId": session["user"]["userId"],
                        "username": session["username"],
                        "image":img
                    },
                ).json()
                trending = trending_ports()
                return render_template(
                    "postSubmitted.html",
                    user=session["user"],
                    name="What Name",
                    trendPorts=trending, ports=trending
                )

            except:
                return render_template(
                    "writePost.html",
                    user=session["user"],
                    error="Invalid Post",
                    trendPorts=trending,
                )
        # If it's  a get
        else:
            ports = trending_ports()
            print(ports)
            return render_template(
                "writePost.html", user=session["user"], trendPorts=trending, ports=ports
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
        trending = trending_ports()
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
            port=post
        )
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
        type = res['type']
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
    trending = trending_ports()
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
                    break
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
        print(res)
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
        session["subscriptions"] = requests.get(
            f"{api}/ports-for-username/", json={"username": username}
        ).json()["all_subscriptions for {data_value}"]
        session.pop("trending", None)
        trending_ports()
        return res
    else:
        return redirect("/login/")

'''
--- POST ---
'''
@app.route("/post/<postId>", methods = ["POST", "GET"])
def post_by_title(postId):
    trending = trending_ports()
    ##Get post by post ID
    post = requests.get(
        f"{api}/post-by-id/",
        json={"id": f"{postId}"}).json()['posts'][0]
    print(post)
    if "loggedin" in session:
        for voted in session["votes"]:
            if voted['postId'] == post['postId']:
                post.update({"upOrDownvoted": voted['vote']})
        post_title = post['postTitle']
        try:
            # post_dict = requests.get(
            #     f"{api}/post-by-title/",
            #     json={"title": title}).json()
            comments_and_reps = requests.get(
                f"{api}/comments-by-post/",
                json={"id": postId}).json()
        except Exception as e:
            print("EXCEPT")
            print(e)
            redirect("/home/")
        if(request.method == "GET"):
            # If you click on subscribe(you just joined the port),
            print(comments_and_reps)
            return render_template('postDetails.html', user = session['user'], name = "Post", post=post, comments= comments_and_reps, trendPorts=trending)
        ## MEANING WE ARE POSTING A COMMENT
        elif(request.method == "POST"):
            res = request.form
            print(res)
            if "loggedin" in session:
            # If you click on subscribe(you just joined the port)
                # text, post_id, parent_id, author
                text = res["commentToPostText"]
                post_id = post["postId"]
                author = session['username']
                try:
                    parent_id = res["parentId"]
                except:
                    parent_id = "NULL"
                print("we got to text")
                print(author)
                try:
                    add_comment = requests.post(
                    f"{api}/add-comment/",
                    json={"text": text, "postId":post_id, "parentId":parent_id, "author":author}).json()
                    print("GOT HERE TOO!")
                    print(add_comment)
                    return render_template('postDetails.html', user = session['user'], name = "Post", post=post, comments = comments_and_reps, commentSubmittedMessage = True, trendPorts=trending)
                except:
                    return redirect("/login/")
    else:
         return redirect("/login/")




# '''
# ---- ADD COMMENT -----
# '''
# @app.route("/add-comment/", methods = ["POST"])
# def add_comment_post():
#     if "loggedin" in session:
#         post_title = title
#     # If you click on subscribe(you just joined the port)
#         # text, post_id, parent_id, author
#         text = res["text"]
#         post_id = res["postId"]
#         parent_id = None
#         author = session['username']
#         try:
#             parent_id = res["parentId"]
#         except:
#         try:
#             add_comment = requests.post(
#                 f"{api}/add-comment/",
#                 json={"text": text, "post_id":post_id, "parent_id":parent_id, "author":author}).json()

#             print(comments)
#             return render_template('postDetails.html', user = session['user'], name = "Post", post=post_dict, comments = comments, commentSubmittedMessage = True)
#         except Exception as e:
#             print(e)
#             return redirect('/home/')
#     else:
#         return redirect("/login/")



"""
 ------PROFILE-----
"""
@app.route("/profile/", methods=["GET", "POST"])
def profile():
    trending = trending_ports()
    if "loggedin" in session:
        print("In User Profile.")

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

            try:
                response = requests.put(api + "/update/",
                data=data,
                headers = headers)
                session["user"]["description"] = form["descriptionTextArea"]
                print("Update description successful!")
            except:
                print("Error: Can't update your description.")
            print(response.content)

            data = json.dumps(
            { "username":session["user"]["username"],
             "field":"avatarUrl",
              "value":form["avatarURL"] })
            print(data)

            try:
                response = requests.put(api + "/update/",
                data=data,
                headers = headers)
                session["user"]["avatarUrl"] = form["avatarURL"]
                print("Update avatarUrl successful!")
            except:
                Print("Error: Can't update your avatarUrl.")
            print(response.content)

        return render_template(
            "userInfo.html",
            userProfile=True,
            name=session["user"]["username"],
            user=session["user"],
            viewedUser=session["user"],
            trendPorts=trending,
        )
    else:
        print("Not loggin yet.")
        return redirect("/login/")



"""
------UPDATE-----
"""
@app.route("/update/", methods=["GET", "POST"])
def update():

    if "loggedin" in session:
        trending = trending_ports()
        form = request.form.to_dict()
        headers = {"Content-Type": "application/json"}

        if request.method == "POST":

            if "emailSetting" in form.keys():

                print("In Account Settings: Email and Password.")
                payload = json.dumps(
                    {
                        "username": session["user"]["username"],
                        "field": "email",
                        "value": form["emailSetting"],
                    }
                )

                try:
                    response = requests.put(api + "/update/",
                    data=payload,
                    headers=headers)
                    #update session's user userInfo
                    session["user"]["email"] = form["emailSetting"]
                    print("Update email successful!")
                except:
                    Print("Error: Can't change your email.")

                print(response.content)

                return render_template(
                    "userInfo.html",
                    name=session["user"]["username"],
                    user=session["user"],
                    accountSettings=True,
                    emailAndPassword=True,
                    trendPorts=trending
                )

            elif "passwordSetting" in form.keys():

                print("In Account Settings: Email and Password.")
                payload = json.dumps(
                    {
                        "username": session["user"]["username"],
                        "field": "password",
                        "value": form["passwordSetting"],
                    }
                )

                try:
                    response = requests.put(api + "/update/",
                    data=payload,
                    headers=headers)
                    #update session's user userInfo
                    session["user"]["password"] = form["passwordSetting"]
                    print("Update password successful!")
                except:
                    Print("Error: Can't change your password.")

                print(response.content)

                return render_template(
                    "userInfo.html",
                    name=session["user"]["username"],
                    user=session["user"],
                    accountSettings=True,
                    emailAndPassword=True,
                    trendPorts=trending
                )
            elif "notifications" in form.keys():

                print("In Account Settings: Notifications.")

                #make it intentional, can't find any api to access these parameters.
                session["user"]["isPostCommentNotificationsEnabled"]=True
                session["user"]["isCommentReplyEnabled"]=True
                session["user"]["isEmailPrivate"]=False

                return render_template(
                    "userInfo.html",
                    name=session["user"]["username"],
                    user=session["user"],
                    notifications=True,
                    accountSettings=True,
                )

            return render_template(
                "userInfo.html",
                name=session["user"]["username"],
                user=session["user"],
                accountSettings=True,
                emailAndPassword=True,
                trendPorts=trending
            )

        else:
            print("In Account Settings: main page.")
            return render_template(
                "userInfo.html",
                name=session["user"]["username"],
                user=session["user"],
                accountSettings=True,
                emailAndPassword=True,
                trendPorts=trending
            )
    else:
        print("Not loggin yet.")
        return redirect("/login/")


"""
------DASHBOARD-----
"""
@app.route("/dashboard/", methods=["GET", "POST"])
def dashBoard():
    if "loggedin" in session:
        trending = trending_ports()

        if request.method == "POST":
            form = request.form.to_dict()

            if "subscriptions" in form.keys():
                try:
                    res = requests.get(
                        f"{api}/ports-for-username/", json={"username": session["user"]["username"]}
                    ).json()["all_subscriptions for {data_value}"]
                except:
                    Print("Error: can't get ports user subscribed.")

                print("In Dashboard subscription.")
                user = session["user"]
                user["myPorts"] = []
                for key in res:
                    temp = {}
                    temp["id"] = key["portId"]
                    temp["name"] = key["portName"]
                    user["myPorts"].append(temp)

                return render_template(
                    "userInfo.html",
                    dashboard=True,
                    subscrptions=True,
                    name=session["user"]["username"],
                    user=user,
                    viewedUser=session["user"],
                    trendPorts=trending,
                )
            elif "comments" in form.keys():

                print("In Dashboard comments.")
                return render_template(
                    "userInfo.html",
                    dashboard=True,
                    comments=True,
                    name=session["user"]["username"],
                    user=session["user"],
                    viewedUser=session["user"],
                    trendPorts=trending,
                )
            elif "savedPosts" in form.keys():
                # port = requests.get(f"{api}/my-posts/", json={"username": session["user"]["username"]}).json()
                # user = session["user"]
                # user["savedPosts"] = []
                # for post in port["posts"]:
                #     temp = {}
                #     temp["totalVotes"] = post["votes"]
                #     temp["portname"] = post["portName"]
                #     temp["title"] = post["postTitle"]
                #     temp["text"] = post["postText"]
                #     temp["dateCreated"] = post["dateCreated"]
                #     temp["avatarUrl"] = post["image"]
                #     user["savedPosts"].append(temp)

                print("In Dashboard savedPosts.")
                return render_template(
                    "userInfo.html",
                    dashboard=True,
                    savedPosts=True,
                    name=session["user"]["username"],
                    user=session["user"],
                    viewedUser=session["user"],
                    trendPorts=trending,
                )
            elif "myPosts" in form.keys():
                print("In Dashboard myPosts.")
                try:
                    posts = requests.get(f"{api}/my-posts/",
                    json={"username": session["user"]["username"]}
                    ).json()
                except:
                    Print("Error: Can't get user's posts.")
                user = session["user"]
                user["myPosts"] = []
                for post in posts["posts"]:
                    temp = {}
                    temp["totalVotes"] = post["votes"]
                    temp["portname"] = post["portName"]
                    temp["title"] = post["postTitle"]
                    temp["text"] = post["postText"]
                    temp["dateCreated"] = post["dateCreated"]
                    temp["commentNum"] = 3
                    temp["imageUrl"] = post["image"]
                    user["myPosts"].append(temp)
                print(user["myPosts"])

                return render_template(
                    "userInfo.html",
                    name=session["user"]["username"],
                    trendPorts=trending,
                    user=user,
                    dashboard=True,
                    myPosts=True
                )

        print("In Dashboard main page.")
        return render_template(
            "userInfo.html",
            dashboard=True,
            user=session["user"],
            name=session["user"]["username"],
            viewedUser=session["user"],
            trendPorts=trending,
        )
    else:
        print("Not loggin yet.")
        return redirect("/login/")

"""
------OUR TEAM PAGE-----
"""
@app.route("/ourteam/")
def ourteam():
    trending = trending_ports()
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
    trending = trending_ports()
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
    trending = trending_ports()
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
    trending = trending_ports()
    return render_template(
        "posts.html",
        name="Bla",
        trendPorts=trending,
        port="Main"
    )


"""
------FORGOTPW-----
"""
@app.route("/forgot/")
def forgot():
    trending = trending_ports()
    return render_template('noPasswordReminders.html', name = "Bla", trendPorts = trending)



@app.route("/Regist_Pending/")
def pending():
    user = session["user"]
    trending = trending_ports()
    return render_template(
        "genLinks.html", name=user["first"], user=user, trendPorts=trending
    )



# helper function to get "trending posts"
# WIll do this by just getting three three random ports
def trending_ports():
    try:
        # tries to return trending ports
        # will only fail if session['trending'] hasn't been initialized
        # which will usually be when a user first comes to the site
        return session['trending']
    except:
        # will only occur when a user first comes to the site or a user logs in or subscribes
        ports = requests.get(f"{api}/allports/").json()
        if "loggedin" in session:
            for subscribe_ports in session['subscriptions']:
                for port in ports['all_ports']:
                    if port['id'] == subscribe_ports['portId']:
                        port.update({"isSubscribed": True})
                        break
        session['trending'] = ports['all_ports']
        return session['trending']




def update_vote_for_post(port):
    if "loggedin" in session:
        try:
            for posts in port["posts"]:
                for votes in session["votes"]:
                    if posts["postId"] == votes["postId"]:
                        # print(votes["vote"])
                        posts.update({"upOrDownvoted": votes["vote"]})
                        break
            return port
        except:

            return redirect('/home/')
    else:
        return None

def load_user(username):
    user = (requests.get(f"{api}/user", json={"username": username}).json())["user"][0]
    print(user)
    return user


if __name__ == "__main__":
    webbrowser.open_new("localhost:8080")
    app.run("localhost", 8080, debug=True)
