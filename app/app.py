from flask import Flask, render_template, request, redirect, jsonify
import requests

app = Flask(__name__)
       


users_db = ["jonnyman"]
# @app.route('/')
# def home():
#     return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def login():
    loggedIn = False
    res = request.form
    user = res['username']
    if (res):
        loggedIn = True
    password = res['password']
    if(user in str(users_db)):
        return render_template('home.html', loggedIn=loggedIn, username=user)
    users_db.append(user)
    print(users_db)
    return render_template('home.html')


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
