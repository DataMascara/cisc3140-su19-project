from flask import Flask, render_template, request, redirect, url_for, session
import requests
import json
import urllib.request
import webbrowser

# Example calling the API from another python file

# Relative path to reach the templates folder
app = Flask(__name__, template_folder='templates')
app.secret_key = "test"

# Assuming the API is running at the local ip below
api = "http://127.0.0.1:5000"

 


def load_user(username):
    user = (requests.get(f"{api}/user", json={
        "user": username}).json())['user'][0]
    print(user)
    return user

@app.route('/', methods=['GET'])
def redirect_home():
    if 'loggedin' in session:
        return redirect("/home/")
    return redirect("/login/")

@app.route('/login/', methods=['POST', 'GET'])
def login_api():
    # already logged in
    if 'loggedin' in session:
        return  redirect("/home/")
    else:
        if request.method == 'POST':
            res = request.form
            print(res)
            # Grab the user and pw
            username = res['username']
            password = res['password']
            api_res = requests.post(f"{api}/login/", json={
                    "username": username, "password": password}).json()
            print(api_res['user']['username'])

            if api_res['user']['username']:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                # session['id'] = account['id']
                session['username'] = username
                session['user'] = api_res['user']
                return render_template('base.html', title='Logged In', user = session['user'])
            else:
                return render_template('base.html', title="", errLogIn=True)
        else:
            print("HELLO")
            return render_template('base.html', title='NONE')



@app.route('/logout/')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
   #Redirect to login page
    return redirect('/home/')


@app.route('/home/')
def home():
    if 'loggedin' in session:
        print(session)
        return render_template('base.html', user = session['user'])
    else:
        return render_template('base.html')

@app.route('/post/', methods=['GET', 'POST'])
def post():
    if 'loggedin' in session:
        print(session)
        if request.method == 'POST':
            try:
                res = request.form
                title = res['title']
                portname = res['portname']
                text = res['text']

                response = (requests.get(f"{api}/newpost/",
                                         json={"title": title, "text": text, "portname": portname,
                                               "userId": session['id'], "username": session['username']}).json())
                print(response)
                return render_template('postSubmitted.html', user=session['user'])
            except:
                return render_template('writePost.html', user= session['user'])
        else:
            return render_template('writePost.html', user=session['user'])

    else:
        return render_template('base.html')


# renders the template to signup
@app.route('/signup/', methods=['POST', 'GET'])
def signup():
    # if loggedin why you signing up
    if 'loggedin' in session:
        return redirect('/home/')
    else:
        # submitting registration
        if request.method == 'POST':
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
                "email": email, "password": password, 'username': username, "first": first, "last": last,
                "avatarurl": avatarurl, "description": description
            }).json()
            print(res)

            try:
                # if this line is successful then the user is created
                session['user'] = res['user']
                session['loggedin'] = True
                # session['id'] = account['id']
                session['username'] = username
                return redirect('/home/')

            except:
                # will redirect you back to signup page if user already exists
                return render_template('register.html')
        # rendering register
        else:
            return render_template('register.html')


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
