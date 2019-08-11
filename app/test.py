# Version 1.1
#    08.09.2019
#    Description: new routes and corresponding functions added (each for every template view).
# Notice: once compiled, this file causes 9 windows opened in the browser.

from flask import Flask, render_template, request
import urllib.request
import webbrowser

app = Flask(__name__, template_folder=r'./templates') # Relative path to reach the templates folder

# Dictionary of a user with only one key (so far)
user = {'username': 'bla-bla-bla'}
# Dictionary of 5 trending ports with two keys for each
trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]

@app.route('/')
def hello():
    return render_template('base.html', name = "Bla", trendPorts = trendPorts)

@app.route('/homepage')
def hello1():
    return render_template('base.html', name = "Bla", trendPorts = trendPorts, user = user)

@app.route('/our-team/')
def hello2():
    return render_template('genLinks.html', name = "Bla", user = user, trendPorts = trendPorts, about = True)

@app.route('/contact-us/')
def hello3():
    return render_template('genLinks.html', name = "Bla", user = user, trendPorts = trendPorts, contact= True)

@app.route('/terms-and-conditions/')
def hello4():
    return render_template('genLinks.html', name = "Bla", user = user, trendPorts = trendPorts, terms = True)

@app.route('/post-submitted/')
def hello5():
    return render_template('postSubmitted.html', name = "Bla", user = user, trendPorts = trendPorts)

@app.route('/write-post/')
def hello6():
    return render_template('writePost.html', name = "Bla", user = user, trendPorts = trendPorts)

@app.route('/registration-pending/')
def hello7():
    return render_template('registPending.html', name = "Bla", user = user, trendPorts = trendPorts)

@app.route('/register/')
def hello8():
    return render_template('register.html', name = "Bla", trendPorts = trendPorts, errUsernameInUse = True)

#----------------- 08.10.2019 ------------------

# Homepage ('posts.html') template rendering below:
# The actual 'homepage' of a user should contain mixture of posts from various subscribed ports.
# Below is an example of just one port.
# The port 'name' for a mixture should be: 'all', and not 'CISCRocks' as below.
# Each dict of 'posts' below will then have to have another key as follows: 'port': {'name': 'bla-bla-port'}

# Example with a port with 4 posts:
posts = [{'id': 256, 'title': 'What I Love about CISC', 'totalVotes': 36, 'image': 'https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940', 'text': 'What a wonderful world!', 'commentNum': 85, 'dateCreated': '2019-08-11 02:23:04', 'username': 'jtoija', 'avatarUrl': 'https://cdn.sandals.com/beaches/v12/images/general/destinations/home/beach.jpg'}, {'id': 257, 'title': 'Want to Order Some Pizza on the Last Day of Classes?', 'totalVotes': 1000, 'image': 'https://cdn.apartmenttherapy.info/image/fetch/f_auto,q_auto:eco/https%3A%2F%2Fstorage.googleapis.com%2Fgen-atmedia%2F3%2F2018%2F03%2F55cd28cae8ee78fe1e52ab1adc9eafff24c9af92.jpeg', 'text': "Why shouldn't we?", 'commentNum': 12000, 'dateCreated': '2019-08-11 02:23:04', 'username': 'mary060196', 'avatarUrl': 'https://cdn.shopify.com/s/files/1/1061/1924/products/Thumbs_Up_Hand_Sign_Emoji_large.png?v=1480481047'}, {'id': 258, 'title': 'What happens if there is no post image?', 'totalVotes': 15, 'image': None, 'text': "Let's see!", 'commentNum': 5, 'dateCreated': '2019-08-11 02:23:04', 'username': 'mary060196', 'avatarUrl': 'https://cdn.shopify.com/s/files/1/1061/1924/products/Thumbs_Up_Hand_Sign_Emoji_large.png?v=1480481047'}, {'id': 259, 'title': 'What if There is Also No Description?', 'totalVotes': 92, 'image': None, 'text': None, 'commentNum': 122, 'dateCreated': '2019-08-11 02:23:04', 'username': 'jtoija', 'avatarUrl': 'https://cdn.sandals.com/beaches/v12/images/general/destinations/home/beach.jpg'}]
port = {'name': 'CISCRocks', 'posts': posts}

# Note the optional 'search' argument passed to the function, and see what happens on the localhost's screen when you run the file!
@app.route('/newsfeed/')
def hello9():
    return render_template('posts.html', name = "Bla", trendPorts = trendPorts, port = port, search = "My First Search!")


#-----------------------------------------------

# 2 Examples of the Display of the Port Index Template

# Create a list of 5 ports dictionaries. The ports are based on the Product Team's 'Port_Index.xlsx' file that is located now in their folder.
ports = [{'id': 1, 'name': 'bcNews', 'mem': 523, 'description': 'A place to post Brooklyn College-wide news and related information.', 'isSubscribed': True},
         {'id': 2, 'name': 'CISC3115', 'mem': 841, 'description': 'Introduction to Programming Using Java: Algorithms, computers and programs.', 'isSubscribed': True},
         {'id': 3, 'name': 'CISC2210', 'mem': 752, 'description': 'Introduction to Discrete Structures: Elementary set theory, functions, relations, and Boolean algebra.', 'isSubscribed': False},
         {'id': 4, 'name': 'csNews', 'mem': 16854, 'description': 'A place to post Brooklyn College Computer Science Department news and related information.', 'isSubscribed': True},
         {'id': 5, 'name': 'sellBooks', 'mem': 11577, 'description': 'A place to advertise books for sale.', 'isSubscribed': False} ]

# Example 1: The user is signed in
@app.route('/port-index/example1')
def hello10():
    return render_template('portIndex.html', name = "Bla", trendPorts = trendPorts, ports = ports, user = user)

# Example 1: The user is signed out
@app.route('/port-index/example2')
def hello11():
    return render_template('portIndex.html', name = "Bla", trendPorts = trendPorts, ports = ports)


if __name__ == "__main__":
    # webbrowser.open_new("http://localhost:8080/")
    # webbrowser.open_new("http://localhost:8080/homepage")
    # webbrowser.open_new("http://localhost:8080/our-team/")
    # webbrowser.open_new("http://localhost:8080/contact-us/")
    # webbrowser.open_new("http://localhost:8080/terms-and-conditions/")
    # webbrowser.open_new("http://localhost:8080/post-submitted/")
    # webbrowser.open_new("http://localhost:8080/write-post/")
    # webbrowser.open_new("http://localhost:8080/registration-pending/")
    # # webbrowser.open_new("http://localhost:8080/register/")
    # webbrowser.open_new("http://localhost:8080/newsfeed/")
    # webbrowser.open_new("http://localhost:8080/port-index/example1")
    # webbrowser.open_new("http://localhost:8080/port-index/example2")
    app.run('localhost', 8080, True, use_reloader=False)
