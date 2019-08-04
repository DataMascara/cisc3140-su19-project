from flask import Flask, render_template, request, url_for
import requests
import json
import urllib.request
import webbrowser

# Example calling the API from another python file

# Relative path to reach the templates folder
app = Flask(__name__)

# Assuming the API is running at the local ip below
api = "http://127.0.0.1:5000/"

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


@app.route('/login/')
def login():

    return render_template('baseLoggedOut.html', title="Logged Out :) ")


if __name__ == "__main__":
    app.run('localhost', 8080, debug=True,)
