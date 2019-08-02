
#------------------------------------------------------------------------------#
# Imports
#------------------------------------------------------------------------------#

# External imports first
# from flask import * # do not use '*'; actually input the dependencies
from flask import Flask, render_template, request, redirect, jsonify
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_cors import CORS

# internal imports next
from database import dbmodule
from config import *

#------------------------------------------------------------------------------#
# App Config
#------------------------------------------------------------------------------#

app = Flask(__name__)
CORS(app)

app.config.from_object('config') # uses settings in config.py
#------------------------------------------------------------------------------#
# Controllers
#------------------------------------------------------------------------------#
#

'''
# Let's assume this app runs backend & front end concurrently
# Thus the root URL / should display the website.
# The api should be accessed from /api/
'''

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():

    # TODO: if user is logged in, username is supplied
    # Currently data comes from config.py's sample data
    # maybe by cookies? username = request.cookies.get('username')


    return render_template('page.html', current_user=current_user,
                                        trendPorts=trending_ports,
                                        user=None)

@app.route('/demo')
def view_demo():
    current_user['username'] = "DEMO_USER" # example for with logged in user

    return render_template('page.html', current_user=current_user,
                                        trendPorts=trending_ports,
                                        user=None)

# Try with chalshaff12 ie /user/
@app.route('/user/<username>')
def test(username):
    # Get the response from the API from the /user endpoint
    res = (requests.get(f"{api}user", json={
           "user": username}).json())['users'][0]
    print(res)
    name = res['first']
    print(name)
    return render_template('page.html', title="Logged In :)", name=name)


'''
ALPHA Back-end API with CRUD(Create, read, update, delete)
for a user-based loggin website.
'''

@app.route('/api/', methods=['GET'])
def api_index():
    return {'hello': 'world'}

'''
-------------Endpoint to login-------------
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
    -Check to see if the email is taken
2)Send json with success response or error if error (implement try blocks?)
'''

@app.route('/api/login/', methods=['POST'])
def api_login():
    res = request.form

    # Grab the user and pw
    user = res['username']
    password = res['password']

    # Get the db query into a python dict
    db_result = json.loads(dbmodule.findUsers('username', user))
    print("dbRes")
    # Grab the first result of users that match
    db_usr = list(db_result['users'])
    print(db_usr)
    # User Validation to DB goes here
    if(len(db_usr) > 0):
        #     #Now that we know the user exists, validate the password
        if (db_usr[0]['password'] == password):
            #         #Send token to allow user to login and advance
            return jsonify({"msg": "Credentials Valid!"}), 200
        else:
            return jsonify({"err": "Credentials Not Valid!"})
    return jsonify({"err": "User Not Valid!"})


'''
-------------Endpoint to CREATE a new user------------- #CREATE (C)RUD
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
    -Check to see if the email is taken
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/api/signup/', methods=['POST', 'GET'])
def sign_up():
    if(request.method == 'POST'):
        # Grab the form
        try:
            res = request.form
            email = res['email']
            username = res['username']
            password = res['password']
            first = res['first']
            last = res['last']
            avatarurl = res['avatarurl']
            added_user = json.loads(dbmodule.insertUser(
                email,  password, username,  first, last, avatarurl))
            pass
        except:
            return jsonify({"err": "Missing Form Data"})

    try:
        return jsonify({"response": added_user['users'][0]}), 201
    except:
        return jsonify({"err": added_user['error']}), 401


'''
-------------Endpoint to GET an existing user-------------#READ from C(R)UD
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
    -Check to see if the email is taken
2)Send json with success response or error if error (implement try blocks?)

'''
@app.route('/api/user/', methods=['GET'])
def user():
    res = request.get_json()  # Grab the response as a python dict from json sent
    # User Validation to DB goes here
    user_wanted = res['user']
    response = json.loads(dbmodule.findUsers("username", user_wanted))
    print(response)
    found = len(response["users"]) > 0
    if found:
        return jsonify(response), 200
    else:
        return jsonify({"error": "User Not Found!"}), 404


@app.route('/api/allusers/')
def all_users():
    return dbmodule.allUsers()


'''
-------------Endpoint to update a user's info-------------
1)Get the user ID
    -Get things they want to change
        -We'll assume one thing changes at a time!
    -Update the database with the things they wanted to edit
        -Front end will do validation?
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/api/update/', methods=['PUT'])
def update_user(user, field):
        # Grab the form data(could also be a json, if we front end sends that instead)
    res = request.form
    thing_to_update = res[field]
    if get_user(user) != '()':  # Currently, the get_user returns '()' if no user is found
        # Call db to do the update on that user's data
        return jsonify({"msg": "Update Success"}), 202
    else:
        # Signal DB Error
        return jsonify({"err": "User Invalid"}), 409
    return jsonify({"err": "Bad request"}), 400


'''
-------------Endpoint to delete a user-------------
1)Get the user ID
    -Update the database with removing the delete
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/api/deleteuser/', methods=['DELETE'])
def delete_user(user):
    # Grab the form data(could also be a json, if we front end sends that instead)
    res = request.form  # Grab the request's form
    user_to_del = user
    if get_user(user) != '()':  # Currently, the get_user returns '()' if no user is found
        # Call db to delete that user's data
        return jsonify({"msg": "Delete Success"}), 202
    else:
        # Signal DB Error
        return jsonify({"err": "User Invalid"}), 409
    return jsonify({"err": "Bad request"}), 400

#------------------------------------------------------------------------------#
# Launch
#------------------------------------------------------------------------------#


if(__name__ == "__main__"):
    app.run(debug=True)
