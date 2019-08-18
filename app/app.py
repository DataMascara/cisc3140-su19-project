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
    # if "loggedin" in session:
    #     return redirect("/home/")
    return redirect("/home/")

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
                    session["comment_votes"] = requests.get(
                        f"{api}/comment-votes-for-username/", json={"username": username}
                    ).json()["voted_data"]
                    trending = trending_ports()
                    session.pop("trending", None)
                    trending = trending_ports()
                    return redirect("/home/")

                    # AB1: This return statement is never reached. Consider deleting.
                    # return render_template(
                    #     "base.html", title="Logged In", user=session["user"]
                    # )
                else:
                    return render_template(
                        "base.html", title="", errLogIn=True, trendPorts=trending
                    )
            except:
                return render_template(
                    "base.html", title="", errLogIn=True, trendPorts=trending
                )
        else:
            return redirect('/home/')



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
    session.pop("comment_votes", None)
    # Redirect to login page
    return redirect("/home/")

"""
-------------HOMEPAGE-------------
"""
@app.route("/home/", methods=["GET", "POST"])
def home():
    # Use the helper method to grab "tredning ports"
    trending = trending_ports()
    posts = requests.get(f"{api}/posts-by-portname/", json={"portname": "Main"}).json()
    sort = "new"
    if request.method == "POST":
        res = request.form
        if res['sortByBtn'] == "hot":
            posts['posts'].sort(key= lambda x:x["votes"], reverse=True)
            sort = "hot"
    # print(post)
    if "loggedin" in session:
        update_vote_for_post(posts)
        return render_template(
            "posts.html",
            name="Home",
            user=session["user"],
            trendPorts=trending,
            port=posts, sort=sort)
    else:
        return render_template(
            "posts.html",
            name="Log In",
            trendPorts=trending,
            port=posts, sort=sort
        )

"""
-------------/PORT(aka subreddit)-------------
- Uses the url to decide what port the user wants to go to.
        - So, this should
"""
@app.route("/p/<portname>/", methods=["GET", "POST"])
def portpost(portname):
    port = requests.get(f"{api}/posts-by-portname/", json={"portname": portname}).json()
    sort = "new"
    if request.method == "POST":
        res = request.form
        if res['sortByBtn'] == "hot":
            port['posts'].sort(key= lambda x:x["votes"], reverse=True)
            sort = "hot"
    print(type(port))
    trending = trending_ports()
    if "loggedin" in session:
        update_vote_for_post(port)
        return render_template(
            "posts.html",
            name="p/" + portname,
            user=session["user"],
            trendPorts=trending,
            port=port, sort=sort
        )
    else:
        return render_template(
            "posts.html",
            name="p/" + portname,
            trendPorts=trending,
            port=port, sort=sort
        )

'''
--------POST HISTORY------
'''
# gets user's post history
@app.route("/u/<username>/posts/", methods=["GET", "POST"])
def my_posts(username):
    trending = trending_ports()
    port = requests.get(f"{api}/my-posts/", json={"username": username}).json()
    if request.method == "POST":
        res = request.form
        if res['sortByBtn'] == "hot":
            port['posts'].sort(key= lambda x:x["votes"], reverse=True)
        if res['sortByBtn'] == "new":
            port['posts'].sort(key=lambda x: x["dateCreated"], reverse=True)
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
            return redirect("/home/")
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
        return redirect("/home/")
        # return render_template(
        #     "base.html", name="Bla", user=session["user"], trendPorts=trending
        # )
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
                    print("the tried")
                    print()
                    if(len(res["postImg"] ) > 3 ):
                        img = res["postImg"]
                    else:
                        img = 'https://i.imgur.com/KdKU0UD.png'
                except:
                    img = 'https://i.imgur.com/KdKU0UD.png'
                # print(img)
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
                session["votes"] = requests.get(
                    f"{api}/votes-for-username/", json={"username": session['username']}
                ).json()["voted_data"]
                return render_template(
                    "postSubmitted.html",
                    user=session["user"],
                    name="What Name",
                    trendPorts=trending, ports=trending, postId=response["posts"][0]["postId"]
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
        return redirect("/home/")

"""
-------------USER SUBSCRIBED POSTS-------------
 - Given a user, return all the posts from the ports they are subscribed to
"""
@app.route("/subscribed-posts/", methods=["GET", "POST"])
def subscribedposts():
    if "loggedin" in session:
        trending = trending_ports()
        posts = requests.get(
            f"{api}/posts-from-subscribed-ports/",
            json={"username": session["username"]},
        ).json()
        sort = "new"
        if request.method == "POST":
            res = request.form
            if res['sortByBtn'] == "hot":
                posts['posts'].sort(key=lambda x: x["votes"], reverse=True)
                sort = 'hot'
        update_vote_for_post(post)
        return render_template(
            "posts.html",
            name="Your feed",
            user=session["user"],
            trendPorts=trending,
            port=posts, sort=sort
        )
    else:
        return redirect("/home/")

'''
----VOTE ON POST----
'''
@app.route("/vote/", methods=["POST"])
def vote():
    if "loggedin" in session:
        res = request.form
        value = res["value"]
        id = res["id"]
        originalValue = res["originalValue"]
        type = res['type']
        # print(res)
        if type == 'post':
            response = (
                requests.post(
                    f"{api}/vote/",
                    json={
                        "username": session["username"],
                        "value": value,
                        "postId": id,
                        "originalValue": originalValue,
                    },
                ).json()
            )["voted_data"]
            session["votes"] = response
        elif type == 'comment':
            response = (
                requests.post(
                    f"{api}/vote-comment/",
                    json={
                        "username": session["username"],
                        "value": value,
                        "commentId": id,
                        "originalValue": originalValue,
                    },
                ).json()
            )["voted_data"]
            session["comment_votes"] = response
        # print(response)
        return "UPDATED"
    else:
        return redirect("/home/")

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
        # session.modified = True
        print(session["subscriptions"])
        trending_ports()
        return res
    else:
        return redirect("/home/")

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
            for votes in session['comment_votes']:
                for comments in comments_and_reps["comments"]:
                    if comments['commentId'] == votes['postId']:
                        comments.update({"upOrDownvoted": votes['vote']})
                for replies in comments_and_reps["replies"]:
                    if replies['commentId'] == votes['postId']:
                        replies.update({"upOrDownvoted": votes['vote']})
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
                    session['comment_votes'] = requests.get(
                        f"{api}/comment-votes-for-username/", json={"username": session['username']}
                    ).json()["voted_data"]
                    comments_and_reps = requests.get(
                        f"{api}/comments-by-post/",
                        json={"id": postId}).json()
                    return render_template('postDetails.html', user = session['user'], name = "Post", post=post, comments = comments_and_reps, commentSubmittedMessage = True, trendPorts=trending)
                except:
                    return redirect("/home/")
    else:
         return redirect("/home/")

"""
 ------PROFILE-----
"""
@app.route("/profile/", methods=["GET", "POST"])
def profile():
    trending = trending_ports()
    if "loggedin" in session:
        print("In User Profile.")
        #check if user visit other's profile
        #receive a json with viewdUser's Name
        #show viewdUser's profile if it exist.
        viewedUser = {}
        res = request.get_json()
        try:
            if 'username' in res:
                if (res["username"] != session["user"]["username"]):
                    viewedUser = requests.get(
                        f"{api}/user/", json={"username": res["username"]}
                    ).json()['user']
                    viewedUser = viewedUser[0]
                else:
                    viewedUser = session["user"]
        except:
            viewedUser = session["user"]
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
                #update session when user update their description.
                session["user"].pop("description", None)
                session["user"]["description"] = form["descriptionTextArea"]
                session.modified = True
                print("Update description successful!")
            except:
                print("Error: Can't update your description.")
            print(response.content)
            data = json.dumps(
            { "username":session["user"]["username"],
             "field":"avatarUrl",
              "value":form["avatarURL"] })
            try:
                response = requests.put(api + "/update/",
                data=data,
                headers = headers)
                #update session when user update their avatarURL.
                session["user"].pop("avatarUrl", None)
                session["user"]["avatarUrl"] = form["avatarURL"]
                session.modified = True
                print("Update avatarUrl successful!")
            except:
                print("Error: Can't update your avatarUrl.")
            print(response.content)
        return render_template(
            "userInfo.html",
            userProfile=True,
            name=session["user"]["username"],
            user=session["user"],
            viewedUser=viewedUser,
            trendPorts=trending,
        )
    else:
        print("Not loggin yet.")
        return redirect("/home/")

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
            #get new email from request, put it in DB
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
                    #update session's user email
                    session["user"].pop("email", None)
                    session["user"]["email"] = form["emailSetting"]
                    session.modified = True
                    print("Update email successful!")
                except:
                    print("Error: Can't change your email.")
                print(response.content)
                return render_template(
                    "userInfo.html",
                    name=session["user"]["username"],
                    user=session["user"],
                    accountSettings=True,
                    emailAndPassword=True,
                    trendPorts=trending
                )
            #get new password, put it into DB
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
                    #update session's user password
                    session["user"].pop("password", None)
                    session["user"]["password"] = form["passwordSetting"]
                    session.modified = True
                    print("Update password successful!")
                except:
                    print("Error: Can't change your password.")
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
                    trendPorts=trending
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
        return redirect("/home/")

"""
------DASHBOARD-----
"""
@app.route("/dashboard/", methods=["GET", "POST"])
def dashBoard():
    if "loggedin" in session:
        trending = trending_ports()
        if request.method == "POST":
            form = request.form.to_dict()
            #if user click subscription
            if "subscriptions" in form.keys():
                #get ports user subscribed
                try:
                    res = requests.get(
                        f"{api}/ports-for-username/", json={"username": session["user"]["username"]}
                    ).json()["all_subscriptions for {data_value}"]
                except:
                    print("Error: can't get ports user subscribed.")
                user = session["user"]
                user["myPorts"] = []
                users = {}
                for key in res:
                    #see how many people subscribed the port
                    try:
                        users = requests.get(
                            f"{api}/users-in-port/", json={"portname": key["portName"]}
                        ).json()["all_subscriptions for {data_value}"]
                    except:
                        print("Error: can't get ports user subscribed.")
                    temp = {}
                    temp["id"] = key["portId"]
                    temp["name"] = key["portName"]
                    temp['mem'] = len(users)
                    temp.update({"isSubscribed": True})
                    user["myPorts"].append(temp)
                    print(user["myPorts"])
                return render_template(
                    "userInfo.html",
                    dashboard=True,
                    subscrptions=True,
                    name=session["user"]["username"],
                    user=user,
                    viewedUser=session["user"],
                    trendPorts=trending,
                )
            #show user's comments
            elif "comments" in form.keys():

                try:
                    res = requests.get(
                        f"{api}/comments-by-user/", json={"username": session["user"]["username"]}
                    ).json()
                    print(res)
                except:
                    print("Error: can't get user's comments.")
                print("In Dashboard Comments.")
                user = session["user"]
                user["myComments"] = []
                #get the user's comments
                for key in res['comments']:
                    #get where comment post and port's info
                    # Need a better way to do this, to many API calls
                    # Maybe add a API endpoint to get all post's with info from one response instead...
                    postInfo = {}
                    print(key)
                    # try:
                    #     postInfo = requests.get(
                    #         f"{api}/post-by-id/", json={"id": key['postId']}
                    #     ).json()['posts'][0]
                    # except:
                    #     print("Error: can't get post and port info.")
                    print(postInfo)
                    temp = {}
                    temp["dateCreated"] = key["dateCreated"]
                    temp["totalVotes"] = key["votes"]
                    temp["text"] = key["commentText"]
                    # temp["portname"] = postInfo["portName"]
                    # temp["postname"] = postInfo["postTitle"]
                    temp["postId"] = key['postId']
                    user["myComments"].append(temp)
                print("In Dashboard comments.")
                return render_template(
                    "userInfo.html",
                    dashboard=True,
                    comments=True,
                    name=session["user"]["username"],
                    user=user,
                    viewedUser=session["user"],
                    trendPorts=trending,
                )
            #show user's saved posts.
            elif "savedPosts" in form.keys():
                posts = requests.get(f"{api}/my-posts/", json={"username": session["user"]["username"]}).json()
                print(posts)
                user = session["user"]
                user["savedPosts"] = []
                ##For now sends User's post's as saved posts..
                for post in posts["posts"]:
                    temp = {}
                    temp["postId"] = post["postId"]
                    temp["totalVotes"] = post["votes"]
                    temp["portname"] = post["portName"]
                    temp["title"] = post["postTitle"]
                    temp["text"] = post["postText"]
                    temp["dateCreated"] = post["dateCreated"]
                    temp["avatarUrl"] = post["image"]
                    user["savedPosts"].append(temp)
                print("In Dashboard savedPosts.")
                return render_template(
                    "userInfo.html",
                    dashboard=True,
                    savedPosts=True,
                    name=session["user"]["username"],
                    user=user,
                    viewedUser=session["user"],
                    trendPorts=trending,
                )
            #show user's posts
            elif "myPosts" in form.keys():
                print("In Dashboard myPosts.")
                try:
                    posts = requests.get(f"{api}/my-posts/",
                    json={"username": session["user"]["username"]}
                    ).json()
                except:
                    print("Error: Can't get user's posts.")
                user = session["user"]
                user["myPosts"] = []
                for post in posts["posts"]:
                    temp = {}
                    temp["postId"] = post["postId"]
                    temp["totalVotes"] = post["votes"]
                    temp["portname"] = post["portName"]
                    temp["title"] = post["postTitle"]
                    temp["text"] = post["postText"]
                    temp["dateCreated"] = post["dateCreated"]
                    temp["commentNum"] = 3
                    temp["imageUrl"] = post["image"]
                    user["myPosts"].append(temp)
                return render_template(
                    "userInfo.html",
                    name=session["user"]["username"],
                    trendPorts=trending,
                    user=user,
                    dashboard=True,
                    myPosts=True
                )
        #defaul display Dashboard
        try:
            res = requests.get(
                f"{api}/ports-for-username/", json={"username": session["user"]["username"]}
            ).json()["all_subscriptions for {data_value}"]
        except:
            print("Error: can't get ports user subscribed.")
        user = session["user"]
        user["myPorts"] = []
        users = {}
        for key in res:
            #see how many people subscribed the port
            try:
                users = requests.get(
                    f"{api}/users-in-port/", json={"portname": key["portName"]}
                ).json()["all_subscriptions for {data_value}"]
            except:
                print("Error: can't get ports user subscribed.")
            temp = {}
            temp["id"] = key["portId"]
            temp["name"] = key["portName"]
            temp['mem'] = len(users)
            temp.update({"isSubscribed": True})
            user["myPorts"].append(temp)
            print(user["myPorts"])
        print("In Dashboard main page.")
        return render_template(
            "userInfo.html",
            dashboard=True,
            user=session["user"],
            name=session["user"]["username"],
            subscrptions=True,
            trendPorts=trending,
        )
    else:
        print("Not loggin yet.")
        return redirect("/home/")

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



@app.route('/search/', methods= ["POST"])
def search():
    user = session["user"]
    trending = trending_ports()
    return render_template('_404Error.html', name = "404", trendPorts = trending, user = user)



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
