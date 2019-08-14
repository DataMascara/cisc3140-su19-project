# Version 1.1
#    08.09.2019
#    Description: new routes and corresponding functions added (each for every template view).
# Notice: once compiled, this file causes 9 windows opened in the browser.

from flask import Flask, render_template, request
import urllib.request
import webbrowser

app = Flask(
    __name__, template_folder=r"./templates"
)  # Relative path to reach the templates folder

# Dictionary of a user with only one key (so far)
user = {"username": "bla-bla-bla"}
# Dictionary of 5 trending ports with two keys for each
trendPorts = [
    {"name": "port1", "mem": 18},
    {"name": "port2", "mem": 17},
    {"name": "port3", "mem": 16},
    {"name": "port4", "mem": 15},
    {"name": "port5", "mem": 14},
]


@app.route("/")
def hello():
    return render_template("base.html", name="Bla", trendPorts=trendPorts)


@app.route("/homepage")
def hello1():
    return render_template("base.html", name="Bla", trendPorts=trendPorts, user=user)


@app.route("/our-team/")
def hello2():
    return render_template(
        "genLinks.html", name="Bla", user=user, trendPorts=trendPorts, about=True
    )


@app.route("/contact-us/")
def hello3():
    return render_template(
        "genLinks.html", name="Bla", user=user, trendPorts=trendPorts, contact=True
    )


@app.route("/terms-and-conditions/")
def hello4():
    return render_template(
        "genLinks.html", name="Bla", user=user, trendPorts=trendPorts, terms=True
    )


@app.route("/post-submitted/")
def hello5():
    return render_template(
        "postSubmitted.html", name="Bla", user=user, trendPorts=trendPorts
    )


@app.route("/write-post/")
def hello6():
    return render_template(
        "writePost.html", name="Bla", user=user, trendPorts=trendPorts
    )


@app.route("/registration-pending/")
def hello7():
    return render_template(
        "registPending.html", name="Bla", user=user, trendPorts=trendPorts
    )


# Two new optional agruments: `username_error` and `email_error` (08.12.2019)
@app.route("/register/")
def hello8():
    return render_template(
        "register.html", name="Bla", trendPorts=trendPorts, username_error = True, email_error = True
    )


# ----------------- 08.10.2019 ------------------

# Homepage ('posts.html') template rendering below:
# The actual 'homepage' of a user should contain mixture of posts from various subscribed ports.
# Below is an example of just one port.
# The port 'name' for a mixture should be: 'all', and not 'CISCRocks' as below.
# Each dict of 'posts' below will then have to have another key as follows: 'port': {'name': 'bla-bla-port'}

# Example with a port with 4 posts:
posts = [
    {
        "id": 256,
        "title": "What I Love about CISC",
        "totalVotes": 36,
        "image": "https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
        "text": "What a wonderful world!",
        "commentNum": 85,
        "dateCreated": "2019-08-11 02:23:04",
        "username": "jtoija",
        "avatarUrl": "https://cdn.sandals.com/beaches/v12/images/general/destinations/home/beach.jpg",
    },
    {
        "id": 257,
        "title": "Want to Order Some Pizza on the Last Day of Classes?",
        "totalVotes": 1000,
        "image": "https://cdn.apartmenttherapy.info/image/fetch/f_auto,q_auto:eco/https%3A%2F%2Fstorage.googleapis.com%2Fgen-atmedia%2F3%2F2018%2F03%2F55cd28cae8ee78fe1e52ab1adc9eafff24c9af92.jpeg",
        "text": "Why shouldn't we?",
        "commentNum": 12000,
        "dateCreated": "2019-08-11 02:23:04",
        "username": "mary060196",
        "avatarUrl": "https://cdn.shopify.com/s/files/1/1061/1924/products/Thumbs_Up_Hand_Sign_Emoji_large.png?v=1480481047",
    },
    {
        "id": 258,
        "title": "What happens if there is no post image?",
        "totalVotes": 15,
        "image": None,
        "text": "Let's see!",
        "commentNum": 5,
        "dateCreated": "2019-08-11 02:23:04",
        "username": "mary060196",
        "avatarUrl": "https://cdn.shopify.com/s/files/1/1061/1924/products/Thumbs_Up_Hand_Sign_Emoji_large.png?v=1480481047",
    },
    {
        "id": 259,
        "title": "What if There is Also No Description?",
        "totalVotes": 92,
        "image": None,
        "text": None,
        "commentNum": 122,
        "dateCreated": "2019-08-11 02:23:04",
        "username": "jtoija",
        "avatarUrl": "https://cdn.sandals.com/beaches/v12/images/general/destinations/home/beach.jpg",
    },
]
port = {"name": "CISCRocks", "posts": posts}

# Note the optional 'search' argument passed to the function, and see what happens on the localhost's screen when you run the file!
@app.route("/newsfeed/")
def hello9():
    return render_template(
        "posts.html",
        name="Bla",
        trendPorts=trendPorts,
        port=port,
        search="My First Search!",
    )


# -----------------------------------------------

# 2 Examples of the Display of the Port Index Template

# Create a list of 5 ports dictionaries. The ports are based on the Product Team's 'Port_Index.xlsx' file that is located now in their folder.
ports = [
    {
        "id": 1,
        "name": "bcNews",
        "mem": 523,
        "description": "A place to post Brooklyn College-wide news and related information.",
        "isSubscribed": True,
    },
    {
        "id": 2,
        "name": "CISC3115",
        "mem": 841,
        "description": "Introduction to Programming Using Java: Algorithms, computers and programs.",
        "isSubscribed": True,
    },
    {
        "id": 3,
        "name": "CISC2210",
        "mem": 752,
        "description": "Introduction to Discrete Structures: Elementary set theory, functions, relations, and Boolean algebra.",
        "isSubscribed": False,
    },
    {
        "id": 4,
        "name": "csNews",
        "mem": 16854,
        "description": "A place to post Brooklyn College Computer Science Department news and related information.",
        "isSubscribed": True,
    },
    {
        "id": 5,
        "name": "sellBooks",
        "mem": 11577,
        "description": "A place to advertise books for sale.",
        "isSubscribed": False,
    },
]

# Example 1: The user is signed in
@app.route("/port-index/example1")
def hello10():
    return render_template(
        "portIndex.html", name="Bla", trendPorts=trendPorts, ports=ports, user=user
    )


# Example 1: The user is signed out
@app.route("/port-index/example2")
def hello11():
    return render_template(
        "portIndex.html", name="Bla", trendPorts=trendPorts, ports=ports
    )

#---------------------------- 08.12.2019 -------------------------

# Examples of Post Details Template

# Create a post dictionary. It will look like this:
postDict = {
    'id': 257, 
    'title': 'Want to Order Some Pizza on the Last Day of Classes?', 
    'portname': "CISCRocks", 
    'totalVotes': 1000, 
    'image': 'https://cdn.apartmenttherapy.info/image/fetch/f_auto,q_auto:eco/https%3A%2F%2Fstorage.googleapis.com%2Fgen-atmedia%2F3%2F2018%2F03%2F55cd28cae8ee78fe1e52ab1adc9eafff24c9af92.jpeg', 
    'text': "Why shouldn't we?", 
    'commentNum': 5, 
    'dateCreated': '2019-08-11 02:23:04', 
    'username': 'mary060196', 
    'avatarUrl': 'https://cdn.shopify.com/s/files/1/1061/1924/products/Thumbs_Up_Hand_Sign_Emoji_large.png?v=1480481047', 
    'upOrDownvoted': 1,
    'comments': [
    {
        'id': 1, 
        'totalVotes': 64, 
        'dateCreated': '2019-08-11 10:10:10', 
        'username': 'jtroia', 
        'avatarUrl': 'https://cdn.sandals.com/beaches/v12/images/general/destinations/home/beach.jpg', 
        'text': "How hadn't I thought of it myself? Great idea!", 
        'upOrDownvoted': 1,
        'comments' : [
        {
            'id': 4, 
            'totalVotes': 24, 
            'dateCreated': '2019-08-11 15:15:15', 
            'username': 'mary060196', 
            'avatarUrl': 'https://cdn.shopify.com/s/files/1/1061/1924/products/Thumbs_Up_Hand_Sign_Emoji_large.png?v=1480481047', 
            'text': "Yea! We'll just have to find a good pizzeria and notify the class.", 
            'upOrDownvoted': 0
        }, 
        {
            'id': 5, 
            'totalVotes': 15, 
            'dateCreated': '2019-08-11 15:20:15', 
            'username': 'jtroia', 
            'avatarUrl': 'https://cdn.sandals.com/beaches/v12/images/general/destinations/home/beach.jpg', 
            'text': "I will send everyone a message on Slack (if anybody even opens it.)", 
            'upOrDownvoted': 0
        }]
    }, 
    {
        'id': 2, 
        'totalVotes': 59, 
        'dateCreated': '2019-08-11 10:20:36', 
        'username': 'bla-bla', 
        'avatarUrl': 'https://www.designrepublic.com/27631-large_default/blabla-big-plexi.jpg', 
        'text': "Bla bla bla bla bla. Bla bla bla bla!", 
        'upOrDownvoted': -1, 
        'comments': []
    }, 
    {
        'id': 3, 
        'totalVotes': 12, 
        'dateCreated': '2019-08-11 10:20:36', 
        'username': 'wowwow1', 
        'avatarUrl': None, 
        'text': "Wow wow wow wow wow. Wow wow wow wow!", 
        'upOrDownvoted': 0, 
        'comments': []
    }]
}

# 'user' is logged in, and optional argument 'commentSubmittedMessage' is passed:
@app.route('/post-details1')
def hello12():
    return render_template('postDetails.html', name = "Bla", trendPorts = trendPorts, post = postDict, user = user, commentSubmittedMessage = True)

# 'user' is logged out:
@app.route('/post-details2')
def hello13():
    return render_template('postDetails.html', name = "Bla", trendPorts = trendPorts, post = postDict)

#---------------------------------- User Info Template --------------------------

# What the 'viewedUser' object must have (this is other than the 'user' dict)
viewedUser1 = {'username': 'mary060196', 'email': 'mary060196@gmail.com', 'avatarUrl': '', 'description': "I love CISC since I was a child.", 'isEmailPrivate': False}
viewedUser2 = {'username': 'jtroia', 'email': 'jtroia@joetroia.com', 'avatarUrl': 'https://cdn.sandals.com/beaches/v12/images/general/destinations/home/beach.jpg', 'description': "Lorem Ipsum ... and other stuff.", 'isEmailPrivate': False}

# We also want to update the 'user' to contain the following:
user = {'username': 'mary060196', 'isEmailPrivate': False, 'isPostCommentNotificationsEnabled': True, 'isCommentReplyEnabled': True}

# Following are 4 example routes for the "Account Settings" and "User Profile" views.
# The third and last "Dashboard" view has not yet been added to the 'userInfo.html' template, but
# it will be added until the 08.13 (maybe including the 08.13).

# 'user' is logged in, and the user is looking at his or her own profile:
@app.route('/user-profile1')
def hello14():
    return render_template('userInfo.html', name = "Bla", trendPorts = trendPorts, viewedUser = viewedUser1, user = user, userProfile = True)

# 'user' is logged in, and the user is looking at somebody else's profile:
@app.route('/user-profile2')
def hello15():
    return render_template('userInfo.html', name = "Bla", trendPorts = trendPorts, viewedUser = viewedUser2, user = user, userProfile = True)

# 'user' is logged in and is looking at the "Account Settings", inside the "Email and Password" tab
# Notice the optional 'errIncorrectPassword' argument that can be passed to show the user message about incorrect current password.
@app.route('/account-settings1')
def hello16():
    return render_template('userInfo.html', name = "Bla", trendPorts = trendPorts, user = user, accountSettings = True, emailAndPassword = True, errIncorrectPassword = True)

# 'user' is logged in and is looking at the "Account Settings", inside the "Notification" tab
@app.route('/account-settings2')
def hello17():
    return render_template('userInfo.html', name = "Bla", trendPorts = trendPorts, user = user, accountSettings = True, notifications = True)

# ------------------------------------- 08.13.2019 Dashboard -----------------------------

# We need to update the 'user' one more time to contain (1) subscribed port data:
myPorts = [ 
  { 
     'id': 1,
     'name': 'port2',
     'mem': 17
   },
  { 
     'id': 2,
     'name': 'CISCRocks',
     'mem': 223
   },  
   { 
     'id': 3,
     'name': 'bcNews',
     'mem': 523
   }
]
# (2) Written comments:
myComments = [ 
   { 
     'postname': "What I Love about CISC",
     'portname': "CISCRocks",
     'totalVotes': 12,
     'text': "There is no more of a professional than you to write such a great post!",
     'dateCreated': '2019-08-19 21:21:21'
   },
  { 
     'postname': "What Classes Do You Take Next Semester?",
     'portname': "bcNews",
     'totalVotes': 19,
     'text': "Computer and Ethics CISC 2820W",
     'dateCreated': '2019-08-15 14:03:45'
   },  
  { 
     'postname': "How Can I deploy an App with Travis CI?",
     'portname': "CISCRocks",
     'totalVotes': 6,
     'text': "Why doing this with Travis CI? Google Cloud is better!",
     'dateCreated': '2019-08-13 07:58:24'
   }
]

# (3) Saved Posts
savedPosts = [ 
   { 
     'title': "What I Love about CISC",
     'portname': "CISCRocks",
     'totalVotes': 36,
     'text': "What a wonderful world!",
     'dateCreated': '2019-08-11 02:23:04',
     'username': 'jtroia',
     'avatarUrl': 'https://cdn.sandals.com/beaches/v12/images/general/destinations/home/beach.jpg'
   },
  { 
     'title': "OK I am Lazy Enough to Write This Post",
     'portname': "offTopic",
     'totalVotes': 10000,
     'text': "Bla Bla squared . . . Bla Bla squared . . . Bla Bla squared . . . Bla Bla squared . . .",
     'dateCreated': '2019-08-11 02:23:04',
     'username': 'bla-bla',
     'avatarUrl': 'https://www.designrepublic.com/27631-large_default/blabla-big-plexi.jpg'
   },  
  { 
     'title': "What to Write about Now?",
     'portname': "offTopic",
     'totalVotes': 100,
     'text': "Bla Bla cubed . . . Bla Bla cubed . . . Bla Bla cubed . . . Bla Bla cubed . . .",
     'dateCreated': '2019-08-11 02:23:04',
     'username': 'bla-bla',
     'avatarUrl': 'https://www.designrepublic.com/27631-large_default/blabla-big-plexi.jpg'
   }
]

# and, finally, written posts:

myPosts = [ 
   { 
     'title': "Bla Bla Post",
     'portname': "CISCRocks",
     'totalVotes': 3,
     'imageUrl': 'https://dxxbxu0f802py.cloudfront.net/wp-content/uploads/2016/07/28093037/feature_are_you_blabla.jpg',
     'commentNum': 55,
     'text': "Just a post",
     'dateCreated': '2019-08-11 02:23:04'
   },
  { 
     'title': "Foo Post",
     'portname': "CISCRocks",
     'totalVotes': 30,
     'imageUrl': None,
     'commentNum': 50,
     'text': "Just a post",
     'dateCreated': '2019-08-11 02:23:04'
   },  
  { 
     'title': "YAML Post",
     'portname': "CISCRocks",
     'imageUrl': None,
     'commentNum': 1000,
     'totalVotes': 300,
     'text': "Just a post",
     'dateCreated': '2019-08-11 02:23:04'
   }
]

# And we put all of these into the user object:
user['myPorts'] = myPorts
user['myComments'] = myComments
user['savedPosts'] = savedPosts
user['myPosts'] = myPosts

# Examples for Dashboard:

# 'user' is logged in and is looking at the "Dashboard" in the section "Subscriptions":
@app.route('/dashboard1')
def hello18():
    return render_template('userInfo.html', name = "Bla", trendPorts = trendPorts, user = user, dashboard = True, subscrptions = True)

# 'user' is logged in and is looking at the "Dashboard" in the section "Comments":
@app.route('/dashboard2')
def hello19():
    return render_template('userInfo.html', name = "Bla", trendPorts = trendPorts, user = user, dashboard = True, comments = True)

# 'user' is logged in and is looking at the "Dashboard" in the section "Saved Posts":
@app.route('/dashboard3')
def hello20():
    return render_template('userInfo.html', name = "Bla", trendPorts = trendPorts, user = user, dashboard = True, savedPosts = True)

# 'user' is logged in and is looking at the "Dashboard" in the section "My Posts":
@app.route('/dashboard4')
def hello21():
    return render_template('userInfo.html', name = "Bla", trendPorts = trendPorts, user = user, dashboard = True, myPosts = True)

#-------------------------- 404 Error & No Password Reminders -------------

# 404 Error Template:
@app.route('/404-error')
def hello22():
    return render_template('_404Error.html', name = "Bla", trendPorts = trendPorts, user = user)

# No "Forgot Password?" Reminders!:
@app.route('/no-such-thing-forgot-password')
def hello23():
    return render_template('noPasswordReminders.html', name = "Bla", trendPorts = trendPorts, user = user)

if __name__ == "__main__":
    # webbrowser.open_new("http://localhost:8181/")
    # webbrowser.open_new("http://localhost:8181/homepage")
    # webbrowser.open_new("http://localhost:8181/our-team/")
    # webbrowser.open_new("http://localhost:8181/contact-us/")
    # webbrowser.open_new("http://localhost:8181/terms-and-conditions/")
    # webbrowser.open_new("http://localhost:8181/post-submitted/")
    # webbrowser.open_new("http://localhost:8181/write-post/")
    # webbrowser.open_new("http://localhost:8181/registration-pending/")
    # webbrowser.open_new("http://localhost:8181/register/")
    # webbrowser.open_new("http://localhost:8181/newsfeed/")
    # webbrowser.open_new("http://localhost:8181/port-index/example1")
    # webbrowser.open_new("http://localhost:8181/port-index/example2")
    # webbrowser.open_new("http://localhost:8181/post-details1")
    # webbrowser.open_new("http://localhost:8181/post-details2")
    # webbrowser.open_new("http://localhost:8181/newsfeed2/")
    # webbrowser.open_new("http://localhost:8181/user-profile1")
    # webbrowser.open_new("http://localhost:8181/user-profile2")
    # webbrowser.open_new("http://localhost:8181/account-settings1")
    # webbrowser.open_new("http://localhost:8181/account-settings2")
    # webbrowser.open_new("http://localhost:8080/dashboard1")
    # webbrowser.open_new("http://localhost:8080/dashboard2")
    # webbrowser.open_new("http://localhost:8080/dashboard3")
    # webbrowser.open_new("http://localhost:8080/dashboard4")
    webbrowser.open_new("http://localhost:8080/404-error")
    # webbrowser.open_new("http://localhost:8080/no-such-thing-forgot-password")
    app.run("localhost", 8181, True, use_reloader=False)

