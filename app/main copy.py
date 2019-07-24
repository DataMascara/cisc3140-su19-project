from flask import Flask, render_template, request, redirect, jsonify
import requests
import os
import json
from database import get_one
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql9299677'
app.config['MYSQL_PASSWORD'] = 'NpxJDZNdlX'
app.config['MYSQL_DB'] = 'sql9299677'
mysql = MySQL(app)
# Dummy DB and Helper Functions

# Grab the dummy db from JSON file in static folder

def data_base():
    filename = os.path.join(app.static_folder, 'db.json')
    with open(filename, 'r') as dbfile:
        data = json.load(dbfile)
    return data

# Takes in the User DB, username and password to validate


users_db = data_base()['users']


def validate_user_cred(the_db, username, password):
    # Go though the users in the db
    for user in the_db:
        # If the username given and password match
        if(user['username'].lower() == username.lower() and user['password'].lower() == password.lower()):
            return True  # Return true
    # If we reach the end, return false(Either user not found or not valid pw)
    return False

# Takes in the User DB, username to validate that they exist


def validate_user(the_db, username):
    # Go though the users in the db
    for user in the_db:
        # If the username given and password match
        if(user['username'].lower() == username.lower()):
            return True  # Return true
            # Otherwise, keep going
    return False  # If we reach the end, return false


@app.route('/', methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        res = request.form
        # Grab the user and pw
        user = res['username']
        password = res['password']
        if(validate_user_cred(users_db, user, password)):
            return render_template('home.html', username=user)
        return jsonify({"error": "Credentials Not Valid!"})
    print(get_one())
    # print(hello())
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if(request.method == 'POST'):
        res = request.form  # Grab the form
        email = res['email']
        user = res['username']
        password = res['password']
        if(validate_user(users_db, user)):
            return jsonify({"error": "User Already Registered"})
        # Signal DB Of new record
        return jsonify({"msg": "User Added"})
    return render_template('signup.html')


@app.route('/delete', methods=['POST', 'GET'])
def test():
    if(request.method == 'POST'):
        res = request.get_json()  # Grab the response as a python dict
        print(type(res))
        user = res['user'].lower()
        print(user)
        return jsonify({"msg": "no result"})


if(__name__ == "__main__"):
    app.run(debug=True)
