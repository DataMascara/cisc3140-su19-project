import requests
import json
import os
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from database import dbmodule


# This is the file that is invoked to start up a development server. It gets a copy of the app from your package and runs it. This won’t be used in production, but it will see a lot of mileage in development.
app = Flask(__name__)
CORS(app)

'''
ALPHA Back-end API with CRUD(Create, read, update, delete)
for a user-based loggin website.
'''


'''
-------------Endpoint to login-------------
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
    -Check to see if the email is taken
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/login/', methods=['POST'])
def login():
    res = request.get_json()
    # Grab the user and pw
    user = res['username']
    password = res['password']

    # Get the db query into a python dict
    db_result = json.loads(dbmodule.users_db.find_users('username', user))

    # Grab the first result of users that match
    db_usr = list(db_result['user'])

    # User Validation to DB goes here
    if(len(db_usr) > 0):
        #     #Now that we know the user exists, validate the password
        if (db_usr[0]['password'] == password):
            #         #Send token to allow user to login and advance
            return jsonify({"user": db_usr[0]}), 200
        else:
            return jsonify({"err": "Credentials Not Valid!"})
    return jsonify({"err": "User Not Valid!"})


'''
-------------Endpoint to CREATE a new user------------- #CREATE (C)RUD
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/signup/', methods=['POST', 'GET'])
def sign_up():
    if(request.method == 'POST'):
        # Grab the form
        res = request.get_json()
        email = res['email']
        username = res['username']
        password = res['password']
        first = res['first']
        last = res['last']
        avatarurl = res['avatarurl']
        description = res["description"] = res["description"]
        added_user = dbmodule.users_db.add_user(
            email,  password, username,  first, last, description, avatarurl)
    try:
        # Returning the added user
        return added_user, 201
    except:
        return jsonify({"err": added_user}), 401


'''
-------------Endpoint to GET an existing user-------------#READ from C(R)UD
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
    -Check to see if the email is taken
2)Send json with success response or error if error (implement try blocks?)

'''
@app.route('/user/', methods=['GET'])
def user():
    res = request.get_json()  # Grab the response as a python dict from json sent
    # User Validation to DB goes here
    user_wanted = res['user']
    response = json.loads(
        dbmodule.users_db.find_users("username", user_wanted))
    print(response)
    found = len(response["user"]) > 0
    if found:
        return jsonify(response), 200
    else:
        return jsonify({"error": "User Not Found!"}), 404


'''
-------------Endpoint to update a user's info-------------
1)Get the user ID
    -Get things they want to change
        -We'll assume one thing changes at a time!
    -Update the database with the things they wanted to edit
        -Front end will do validation?
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/update/', methods=['PUT'])
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
@app.route('/deleteuser/', methods=['DELETE'])
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

# return ports from database
@app.route('/ports/')
def get_ad():
    ports = dbmodule.ports_db.all_ports()
    return ports

# return ports from database
@app.route('/newpost/', methods=['POST'])
def new_post():
    res = request.get_json()  # Grab the response as a python dict from json sent
    # User Validation to DB goes here
    title = res['title']
    text = res['text']
    portname = res['portname']
    username = res['username']
    user_id = json.loads(dbmodule.users_db.find_users(
        "username", username))['user'][0]['userId']

    # Returns the added post from this user
    response = json.loads(
        dbmodule.posts_db.add_post(title, text, portname, user_id, username))

    # Filter out the new one by title, and return that.
    return response


# Function dbmodule.posts_db.all_posts_by(column_name, data_value)
# dbmodule.posts_db.all_posts_by('portId', 1)
# dbmodule.posts_db.all_posts_by('portName', 'main')
@app.route('/posts-by-portname/')
def get_posts():
    port_name = "Main"
    return dbmodule.posts_db.all_posts_by('portName', 'Main')


# Display Posts Relevant to User Given a User id
# Obtain the ids of all the Ports to which the User is subscribed
@app.route('/posts-for-username/')
def get_posts_username():
    res = request.get_json()
    username = res["username"]
    # Clean up result here
    return dbmodule.subscriptions_db.all_subscriptions_by('username', username)


@app.route('/subscribe-to-port/')
def subscribe_to_port():
    res = request.get_json()
    username = res["username"]
    portname = res["portname"]
    # Clean up result here
    return dbmodule.subscriptions_db.add_subscription(username, portname)


'''
---- Getting All Users ----
'''
@app.route('/allusers/')
def all_users():
    return json.loads(dbmodule.users_db.all_users())


if(__name__ == "__main__"):
    app.run(debug=True)
