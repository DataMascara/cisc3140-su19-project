from flask import Flask, render_template, request, redirect, jsonify
import requests
import os
import json
from database import get_user
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql9299677'
app.config['MYSQL_PASSWORD'] = 'NpxJDZNdlX'
app.config['MYSQL_DB'] = 'sql9299677'
mysql = MySQL(app)

'''
ALPHA Back-end API with CRUD(Create, read, update, delete)
for a user-based loggin website.
'''

'''
!!Endpoint to login!!
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
    -Check to see if the email is taken
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/login', methods=['POST'])
def login():
    res = request.form
    # Grab the user and pw
    user = res['username']
    password = res['password']
    # User Validation to DB goes here
    if get_user(user):
        return jsonify({"msg": "Logged in"}), 200
    else:
        return jsonify({"error": "Credentials Not Valid!"})
    return jsonify({"error": "Credentials Not Valid!"})


'''
!!Endpoint to CREATE a new user!! #CREATE (C)RUD
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
    -Check to see if the email is taken
2)Send json with success response or error if error (implement try blocks?) 
'''
@app.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if(request.method == 'POST'):
        # Grab the form
        res = request.form
        email = res['email']
        user = res['username']
        password = res['password']
    # Validate Email is not taken!
    # Add user record to the db
    if get_user(user):
        return jsonify({"msg": "Signed up"}), 201
    else:
        return jsonify({"error": "Email Already Registered"}), 409
    return jsonify({"msg": "Error"}), 401


'''
!!Endpoint to GET an existing user!!#READ from C(R)UD
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
    -Check to see if the email is taken
2)Send json with success response or error if error (implement try blocks?)

'''
@app.route('/user', methods=['GET'])
def user():
    res = request.get_json()  # Grab the response as a python dict from json sent
    # User Validation to DB goes here
    user_wanted = res['user']
    if get_user(user_wanted) != '()':  # Currently, the get_user returns '()' if no user is found
        return jsonify({"msg": "User found!"}), 200
    else:
        return jsonify({"error": "User Not Found!"}), 404
    return jsonify({"error": "Credentials Not Valid!"})


'''
!!Endpoint to update a user's info!!
1)Get the user ID
    -Get things they want to change
        -We'll assume one thing changes at a time!
    -Update the database with the things they wanted to edit
        -Front end will do validation?
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/update', methods=['PUT'])
def update_user(user, field):
        # Grab the form data(could also be a json, if we front end sends that instead)
    res = request.form
    thing_to_update = res[field]
    if get_user(user) != '()':  # Currently, the get_user returns '()' if no user is found
        # Call db to do the update on that user's data
        return jsonify({"msg": "Update Success"}), 202
    else:
        # Signal DB Error
        return jsonify({"error": "User Invalid"}), 409
    return jsonify({"Error": "Bad request"}), 400


'''
!!Endpoint to delete a user!!
1)Get the user ID
    -Update the database with removing the delete
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/deleteuser', methods=['DELETE'])
def delete_user(user):
    # Grab the form data(could also be a json, if we front end sends that instead)
    res = request.form  # Grab the request's form
    user_to_del = user
    if get_user(user) != '()':  # Currently, the get_user returns '()' if no user is found
        # Call db to delete that user's data
        return jsonify({"msg": "Delete Success"}), 202
    else:
        # Signal DB Error
        return jsonify({"error": "User Invalid"}), 409
    return jsonify({"Error": "Bad request"}), 400


if(__name__ == "__main__"):
    app.run(debug=True)
