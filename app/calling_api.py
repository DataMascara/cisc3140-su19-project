from flask import Flask, render_template, request, redirect
import requests
import json
import urllib.request
import webbrowser

# Example calling the API from another python file

# Relative path to reach the templates folder
app = Flask(__name__, template_folder=r'./templates')

# Assuming the API is running at the local ip below
api = "http://127.0.0.1:5000"




@app.route('/api/login/', methods=['POST'])
def login_api():
    res = request.form
    # Grab the user and pw
    user = res['username']
    pw = res['password']
    print(user)
    res = requests.post(f"{api}/login/", json={
           "user": user, "password":pw }).json()["usr"]
    print(res)
    name = res['first']
    print(name)
    return render_template('base.html', title="Logged In :)", user=res)


@app.route('/api/signup/', methods=['POST'])
def login():
    res = request.form
    # Grab the user and pw

        # Grab the form
    res = request.form
    email = res['email']
    username = res['username']
    password = res['password']
    first = res['first']
    last = res['last']
    avatarurl = res['avatarurl']
    description = res["description"]
    email, password, username, first, last, avatarurl
    res = requests.post(f"{api}/signup/", json={
           "email": email, "password":password, 'username':username, "first":first, "last":last, "avatarurl":avatarurl, "description":description }).json()
    print(res)
    # name = res['first']
    # print(name)
    return render_template('base.html', title="Logged In :)", user=res)



@app.route('/Write_Post/')
def create():
    user = {'username': 'bla-bla-bla'}
    trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]
    return render_template('writePost.html', name = "Bla", user = user, trendPorts = trendPorts)

@app.route('/Regist_Pending/')
def pending():
    user = {'username': 'bla-bla-bla'}
    trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]
    return render_template('genLinks.html', name = "Bla", user = user, trendPorts = trendPorts)

@app.route('/Our_Team/')
def team():
    trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]
    return render_template('genLinks.html', name = "Bla", trendPorts = trendPorts)

@app.route('/Post_Submitted/')
def subm():
    user = {'username': 'bla-bla-bla'}
    trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]
    return render_template('postSubmitted.html', name = "Bla", user = user, trendPorts = trendPorts)


@app.route('/api/logout/',methods=['POST', 'GET'])
def logout():
    if(request.method == 'POST'):
        return redirect('/api/login/', code=307)

    return render_template('base.html', title="Logged Out :) ")


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True,)




# Now run this file and navigate to the route below
# Try with chalshaff12 ie /user/
@app.route('/user/<username>')
def test(username):
    # Get the response from the API from the /user endpoint
    res = (requests.get(f"{api}user", json={
           "user": username}).json())['users'][0]
    print(res)
    name = res['first']
    print(name)
    return render_template('baseLoggedIn.html', title="Logged In :)", name=name)
