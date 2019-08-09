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


if __name__ == "__main__":
    webbrowser.open_new("http://localhost:8080/")
    webbrowser.open_new("http://localhost:8080/homepage")
    webbrowser.open_new("http://localhost:8080/our-team/")
    webbrowser.open_new("http://localhost:8080/contact-us/")
    webbrowser.open_new("http://localhost:8080/terms-and-conditions/")
    webbrowser.open_new("http://localhost:8080/post-submitted/")
    webbrowser.open_new("http://localhost:8080/write-post/")
    webbrowser.open_new("http://localhost:8080/registration-pending/")
    webbrowser.open_new("http://localhost:8080/register/")
    app.run('localhost', 8080, True, use_reloader=False)
