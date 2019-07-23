from flask import Flask, render_template, request, redirect, jsonify
import requests, os, json

app = Flask(__name__)
       
#Grab the dummy db from JSON file in static folder       
def data_base():
    filename = os.path.join(app.static_folder, 'db.json')
    with open(filename, 'r') as dbfile:
        data = json.load(dbfile)
    return data

# Grab the users from the "db"
users_db = data_base()['users']

#Takes in the User DB, username and password to validate
def validate_user(the_db, username, password):
    # Go though the users in the db
    for user in the_db:
        # If the username given and password match
        if( user['username'].lower() == username.lower() and user['password'].lower() ==password.lower()):
            return True # Return true
            #Otherwise, keep going
    return False # If we reach the end, return false(Either user not found or not valid pw)


@app.route('/', methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        res = request.form
        if (res): #Flag for being logged in or no
            loggedIn = True
        # Grab the user and pw
        user = res['username']
        password = res['password']
        if(validate_user(users_db,user,password)):
            return render_template('home.html', loggedIn=loggedIn, username=user)
        return render_template('home.html')
    return render_template('home.html')

if(__name__ == "__main__"):
        app.run(debug=True)

# @app.route('/signup')
# def signup():
#     return render_template('sign_up.html')


# @app.route('/addUser', methods=['POST', 'GET'])
# def addUser():
#     req = request.form
#     if controller.addUser(req['firstName'], req['lastName'], req['email'], req['password']):
#         return redirect('/accountCreated')
#     else:
#         return render_template('account_error.html')


# @app.route('/accountCreated')
# def accountCreated():
#     return render_template('account_created.html')


# @app.route('/deleteUser', methods=['POST', 'GET'])
# def deleteUser():
#     req = request.form
#     if controller.deleteUser(req['email']):
#         return redirect('/accountDeleted')
#     else:
#         return render_template('account_error.html')


# @app.route('/accountDeleted')
# def accountDeleted():
#     return render_template('account_deleted.html')


# @app.route('/allAccounts')
# def allAccounts():
#     return controller.getAll()
# #
# # @login_manager.user_loader()
# # def user_loader(user_id):
# #     return controller.findUserByID(user_id)
