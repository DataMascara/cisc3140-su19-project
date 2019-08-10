from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import urllib.request
import webbrowser

# Example calling the API from another python file

# Relative path to reach the templates folder
app = Flask(__name__, template_folder=r'./templates')

# Assuming the API is running at the local ip below
api = "http://127.0.0.1:5000"


@app.route('/')
def home():
    return render_template('base.html')

# possible to make an endpoint private unless redirected to it?
@app.route('/user/<username>/', methods=['GET'])
def user_logged_in(username):
    try:
        user = (requests.get(f"{api}/user", json={
            "user": username}).json())['user'][0]
        print(user)
        return render_template('base.html', user=user)
    except:
        return redirect('/')


@app.route('/user/<username>/post/', methods=['GET', 'POST'])
def post(username):
    # makes sure user posting exists
    try:
        user = (requests.get(f"{api}/user", json={
            "user": username}).json())['user'][0]
        # submitting the post
        if request.method == 'POST':
            try:
                # Grab the form data
                user_id = user['userId']
                res = request.form
                title = res['title']
                portname = res['portname']
                # username name value no longer needed we can get the user from the url
                user = res['username']
                text = res['text']
                # Uncomment once the endpoint is running
                response = (requests.get(f"{api}/newpost/",
                                         json={
                                             "title": title, "text": text, "portname": portname, "userId": user_id}).json())
                print(f" THE RESPONSE {response}")
                return render_template('postSubmitted.html', user=user)

            # if post is unsuccessful returns back to writePost
            except Exception as err:
                print(err)
                return render_template('writePost.html', user=user)

        # rendering writePost
        else:
            return render_template('writePost.html', user=user)

    # returns to homepage
    except:
        return redirect('/')

# @app.route('/api/submitpost/', methods=['POST'])
# def submit_post():
#     try:
#         res = request.form
#         title = res['title']
#         port = res['portname']
#         user = res['username']
#         text = res['text']
#         # print(title + port + user + text)
#         user = (requests.get(f"{api}/user", json={
#             "user": user}).json())['user'][0]
#         return render_template('postSubmitted.html', user=user)
#     except:
#         return redirect('/')


@app.route('/api/login/', methods=['POST'])
def login_api():
    res = request.form
    # Grab the user and pw
    username = res['username']
    pw = res['password']
    try:
        api_res = requests.post(f"{api}/login/", json={
            "username": username, "password": pw}).json()["user"]
        print(res)
        if(pw == api_res["password"]):
            # return render_template('base.html', title="Logged In :)", user=api_res)
            # redirects to /user/<username> endpoint
            return redirect(url_for('user_logged_in', username=username))
        name = res['first']
        print(name)
    except:
        return render_template('base.html', title="", errLogIn=True)


# renders the template to signup
@app.route('/signup', methods=['GET'])
def signup():
    return render_template('register.html')

# calls the api to sign the user up
@app.route('/api/signup', methods=['POST', 'GET'])
def signingup():
    # Grab the form
    res = request.form
    email = res['Email']
    username = res['Username']
    password = res['password']
    first = res['First Name']
    last = res['Last Name']
    # avatarurl = res['imageUpload']
    avatarurl = ''
    # currently signup page has no description box
    # description = res["description"]
    description = ''
    res = requests.post(f"{api}/signup/", json={
        "email": email, "password": password, 'username': username, "first": first, "last": last, "avatarurl": avatarurl, "description": description
    }).json()
    # prints -1 if the user doesn't already exist
    print(res['err'].find('Duplicate'))
    if res['err'].find('Duplicate') == -1:
        # logs the new user in
        # redirects to /user/<username> endpoint
        return redirect(url_for('user_logged_in', username=username))
    else:
        # will redirect you back to signup page if user already exists
        return redirect('/signup')

# @app.route('/api/submitpost/', methods=['POST'])
# def submit_post():
#     trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]
#     res = request.form
#     title = res['title']
#     text = res['text']
#     portname = res['portname']
#     user = res["username"]
#     (title, text, portname, 1)
#     api_res = requests.post(f"{api}/newpost/", json={
#            "title": title, "text":text, 'portname':portname, "user":user
#            }).json()
#     print(api_res)
#     return render_template('postSubmitted.html', name = "Bla", trendPorts = trendPorts, user = "Logged in")


@app.route('/newpost/')
def create():
    trendPorts = [{'name': 'port1', 'mem': 18}, {'name': 'port2', 'mem': 17}, {
        'name': 'port3', 'mem': 16}, {'name': 'port4', 'mem': 15}, {'name': 'port5', 'mem': 14}]
    return render_template('writePost.html', name="Bla", trendPorts=trendPorts, user="Logged in")


@app.route('/Regist_Pending/')
def pending():
    user = {'username': 'bla-bla-bla'}
    trendPorts = [{'name': 'port1', 'mem': 18}, {'name': 'port2', 'mem': 17}, {
        'name': 'port3', 'mem': 16}, {'name': 'port4', 'mem': 15}, {'name': 'port5', 'mem': 14}]
    return render_template('genLinks.html', name="Bla", user=user, trendPorts=trendPorts)


@app.route('/our_team/')
def team():
    trendPorts = [{'name': 'port1', 'mem': 18}, {'name': 'port2', 'mem': 17}, {
        'name': 'port3', 'mem': 16}, {'name': 'port4', 'mem': 15}, {'name': 'port5', 'mem': 14}]
    return render_template('genLinks.html', name="Bla", trendPorts=trendPorts)


@app.route('/Post_Submitted/')
def subm():
    user = {'username': 'bla-bla-bla'}
    trendPorts = [{'name': 'port1', 'mem': 18}, {'name': 'port2', 'mem': 17}, {
        'name': 'port3', 'mem': 16}, {'name': 'port4', 'mem': 15}, {'name': 'port5', 'mem': 14}]
    return render_template('postSubmitted.html', name="Bla", user=user, trendPorts=trendPorts)


@app.route('/api/logout/', methods=['POST', 'GET'])
def logout():
    if(request.method == 'POST'):
        return redirect('/api/login/', code=307)

    return render_template('base.html', title="Logged Out :) ")


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True,)


# Now run this file and navigate to the route below
# Try with chalshaff12 ie /user/
# @app.route('/user/<username>')
# def test(username):
#     # Get the response from the API from the /user endpoint
#     res = (requests.get(f"{api}/user", json={
#            "user": username}).json())['user'][0]
#     print(res)
#     name = res['first']
#     print(name)
#     return render_template('base.html', title="Logged In :)")
