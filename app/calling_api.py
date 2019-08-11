from flask import Flask, render_template, request, redirect, url_for, session
import requests
import json
import urllib.request
import webbrowser

# Example calling the API from another python file

# Relative path to reach the templates folder
app = Flask(__name__, template_folder="templates")
app.secret_key = "test"

# Assuming the API is running at the local ip below
api = "http://127.0.0.1:5000"


@app.route("/", methods=["GET"])
def redirect_home():
    if "loggedin" in session:
        return redirect("/home/")
    return redirect("/login/")


@app.route("/login/", methods=["POST", "GET"])
def login_api():
    # already logged in
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
            print(api_res["user"]["username"])

            if api_res["user"]["username"]:
                # Create session data, we can access this data in other routes
                session["loggedin"] = True
                # session['id'] = account['id']
                session["username"] = username
                session["user"] = api_res["user"]
                return render_template(
                    "base.html", title="Logged In", user=session["user"]
                )
            else:
                return render_template("base.html", title="", errLogIn=True)
        else:
            return render_template("base.html", title="NONE")


@app.route("/logout/")
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    session.pop("user", None)
    # Redirect to login page
    return redirect("/home/")


@app.route("/home/", methods=['GET'])
def home():

    print(session)
    port = (requests.get(
        f"{api}/posts-by-portname/",
        json={
            "portname": "Main"
        }).json())
    print(port)
    trendPorts = [
        {"name": "port1", "mem": 18},
        {"name": "port2", "mem": 17},
        {"name": "port3", "mem": 16},
        {"name": "port4", "mem": 15},
        {"name": "port5", "mem": 14},
    ]
    if "loggedin" in session:
        return render_template('posts.html', name="Bla", user= session['user'], trendPorts=trendPorts, port=port, search="My First Search!")
    else:
        return render_template('posts.html', name="Bla", trendPorts=trendPorts, port=port, search="My First Search!")


@app.route("/p/<portname>", methods=["GET"])
def portpost(portname):
    port = requests.get(
        f"{api}/posts-by-portname/",
        json={
            "portname": portname
        }).json()
    trendPorts = [
        {"name": "port1", "mem": 18},
        {"name": "port2", "mem": 17},
        {"name": "port3", "mem": 16},
        {"name": "port4", "mem": 15},
        {"name": "port5", "mem": 14},
    ]
    if "loggedin" in session:
        return render_template('posts.html', name="Bla", user= session['user'], trendPorts=trendPorts, port=port, search="My First Search!")
    else:
        return render_template('posts.html', name="Bla", trendPorts=trendPorts, port=port, search="My First Search!")

# # renders the template to signup
# @app.route('/signup/', methods=['POST', 'GET'])
# def signup():
#     return render_template('register.html')

# Get's your posts (As json right now)
@app.route("/my-posts/", methods=["GET"])
def my_posts():
    res = requests.get(f"{api}/myposts/", json={"username": session["username"]}).json()
    return res
    # return render_template('register.html')


# calls the api to sign the user up
@app.route("/signup/", methods=["POST", "GET"])
def sign_up():
    # if loggedin why you signing up
    if "loggedin" in session:
        return redirect("/home/")
    # TODO: Remove psudo tending ports for real ones
    trendPorts = [
        {"name": "port1", "mem": 18},
        {"name": "port2", "mem": 17},
        {"name": "port3", "mem": 16},
        {"name": "port4", "mem": 15},
        {"name": "port5", "mem": 14},
    ]
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
        try:
            res = requests.post(
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
            print(f"API Res {res}")
        except:  # Signal the error
            return render_template("register.html", errUsernameInUse=res)
        # if this line is successful then the user is created
        # Load uses helper method returns the dict of the user representation for local storage
        session["user"] = load_user(username)
        session["loggedin"] = True
        # session['id'] = account['id']
        session["username"] = username
        redirect("/home/")
        return render_template(
            "base.html", name="Bla", trendPorts=trendPorts, user=session["user"]
        )
    else:
        return render_template("register.html")


@app.route("/new-post/", methods=["GET", "POST"])
def post():

    # Make sure the user is logged in
    if "loggedin" in session:
        # If we are making a post
        if request.method == "POST":
            try:
                res = request.form
                title = res["title"]
                portname = res["portname"]
                text = res["text"]
                response = requests.get(
                    f"{api}/newpost/",
                    json={
                        "title": title,
                        "text": text,
                        "portname": portname,
                        "userId": session["id"],
                        "username": session["username"],
                    },
                ).json()
                print(response)
                return render_template(
                    "postSubmitted.html",
                    user=session["user"],
                    name="What Name",
                    trendPorts=trendPorts,
                )

            except:
                return render_template(
                    "writePost.html", user=session["user"], error="Invalid Post"
                )
        # If the post fails, try again
        else:
            return render_template("writePost.html", user=session["user"])

    else:
        return render_template("base.html")


@app.route("/subscribed-posts/", methods=["GET"])
def subscribedposts():
    if 'loggedin' in session:
        post = requests.get(
            f"{api}/posts-from-subscribed-ports/",
            json={
                "username": session["username"]
            }).json()

        return post
    else:
        return redirect('/login/')


@app.route("/ourteam/")
def ourteam():
    if "loggedin" in session:
        return render_template("genLinks.html", user=session["user"], about=True)
    else:
        return render_template("genLinks.html", about=True)


@app.route("/contact/")
def contact():
    if "loggedin" in session:
        return render_template("genLinks.html", user=session["user"], contact=True)
    else:
        return render_template("genLinks.html", contact=True)


@app.route("/terms/")
def terms():
    if "loggedin" in session:
        return render_template("genLinks.html", user=session["user"], terms=True)
    else:
        return render_template("genLinks.html", terms=True)


@app.route("/newsfeed/")
def hello9():
    return render_template(
        "posts.html", name="Bla", trendPorts="", port="Main", search="My First Search!"
    )


@app.route("/Regist_Pending/")
def pending():
    user = {"username": "bla-bla-bla"}
    trendPorts = [
        {"name": "port1", "mem": 18},
        {"name": "port2", "mem": 17},
        {"name": "port3", "mem": 16},
        {"name": "port4", "mem": 15},
        {"name": "port5", "mem": 14},
    ]
    return render_template(
        "genLinks.html", name="Bla", user=user, trendPorts=trendPorts
    )


def load_user(username):
    user = (requests.get(f"{api}/user", json={"username": username}).json())["user"][0]
    print(user)
    return user


if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)

