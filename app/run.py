import json, os, requests
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from app.database import dbmodule
## This is the file that is invoked to start up a development server. It gets a copy of the app from your package and runs it. This won’t be used in production, but it will see a lot of mileage in development.
app = Flask(__name__)
CORS(app)

'''
ALPHA Back-end API with CRUD(Create, read, update, delete)
for a user-based loggin website.
'''

#Test route if sending username directly
@app.route('/test/<username>', methods=['GET'])
def usertest(username):
    # res = request.get_json()  # Grab the response as a python dict from json sent
    # # User Validation to DB goes here
    user_wanted = username
    response = json.loads(dbmodule.users_db.find_users("username", user_wanted))
    print(response)
    found = len(response["users"]) > 0
    if found:
        return jsonify(response), 200
    else:
        return jsonify({"error": "User Not Found!"}), 404

#Test route if sending username and password via json 
@app.route('/test/testuser', methods=['GET'])
def usertest1(username):
    res = request.get_json()  # Grab the response as a python dict from json sent
    # # User Validation to DB goes here
    user_wanted = res["username"]
    response = json.loads(dbmodule.users_db.find_users("username", user_wanted))
    print(response)
    found = len(response["users"]) > 0
    if found:
        return jsonify(response), 200
    else:
        return jsonify({"error": "User Not Found!"}), 404


'''
-------------Endpoint to login-------------
1)Get the user details from front end (either from form or json)
    -Front end will do validation on length and ensure client-side error checking
    -Check to see if the email is taken
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/login/', methods=['POST'])
def login():
    res = request.form

    # Grab the user and pw
    user = res['username']
    password = res['password']

    # Get the db query into a python dict
    # Checks if user is logging in with a email or username
    if user.find('@') > -1 and user.find('.') > -1:
        db_result = json.loads(dbmodule.users_db.find_users('email', user))
    else:
        db_result = json.loads(dbmodule.users_db.find_users('username', user))
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
@app.route('/signup/', methods=['POST', 'GET'])
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
            description = res['description']
            avatarurl = res['avatarurl']
            added_user = json.loads(dbmodule.users_db.add_user(
                email,  password, username,  first, last, description, avatarurl))
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
@app.route('/user/', methods=['GET'])
def user():
    res = request.get_json()  # Grab the response as a python dict from json sent
    # User Validation to DB goes here
    user_wanted = res['user']
    response = json.loads(dbmodule.users_db.find_users("username", user_wanted))
    print(response)
    found = len(response["users"]) > 0
    if found:
        return jsonify(response), 200
    else:
        return jsonify({"error": "User Not Found!"}), 404


@app.route('/allusers/')
def all_users():
    return dbmodule.users_db.all_users()


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
def update_user():
        # Grab the form data(could also be a json, if we front end sends that instead)
    res = request.form
    username = res['username']
    field_value = res['field']
    new_value = res['value']
    return jsonify(dbmodule.users_db.update_user(username, field_value, new_value)), 200
    # if dbmodule.users_db.find_users(user) != '()':  # Currently, the get_user returns '()' if no user is found
    #     # Call db to do the update on that user's data
    #     return jsonify({"msg": "Update Success"}), 202
    # else:
    #     # Signal DB Error
    #     return jsonify({"err": "User Invalid"}), 409
    # return jsonify({"err": "Bad request"}), 400


'''
-------------Endpoint to delete a user-------------
1)Get the user ID
    -Update the database with removing the delete
2)Send json with success response or error if error (implement try blocks?)
'''
@app.route('/deleteuser/', methods=['DELETE'])
def delete_user():
    # Grab the form data(could also be a json, if we front end sends that instead)
    res = request.form  # Grab the request's form
    user_to_delete = res['username']
    response = json.loads(dbmodule.users_db.find_users("username", user_to_delete))
    # print(response)
    found = len(response["users"]) > 0
    if found:
        return jsonify(dbmodule.users_db.delete_user(user_to_delete)), 200
    else:
        return jsonify({"error": "User Not Found!"}), 404


#try to get the port that user subscribed.
#it should return the name of port and number of menber in port
#the database module hasn't such function yet.
#if they did it, I can try to implement it.
# @app.route('/port/', methods=['GET'])
# def port():
#     res = request.get_json()
#     username = res['user']
    #response = json.loads(dbmodule.findPort("username", user_wanted))
    #found = len(response["name"]) > 0
    # if found:
    #     return jsonify(response), 200
    # else:
    #     return jsonify({"error": "User Not Found!"}), 404


if(__name__ == "__main__"):
    app.run(debug=True)
