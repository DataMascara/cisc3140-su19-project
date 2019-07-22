from flask import Flask, render_template, request, redirect
from flask_login import LoginManager
from db_controller import Controller

app = Flask(__name__)

# Creates the database controller with the url as the parameter
controller = Controller('sqlite:///users.db')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    req = request.form



@app.route('/signup')
def signup():
    return render_template('sign_up.html')


@app.route('/addUser', methods=['POST', 'GET'])
def addUser():
    req = request.form
    if controller.addUser(req['firstName'], req['lastName'], req['email'], req['password']):
        return redirect('/accountCreated')
    else:
        return render_template('account_error.html')


@app.route('/accountCreated')
def accountCreated():
    return render_template('account_created.html')


@app.route('/deleteUser', methods=['POST', 'GET'])
def deleteUser():
    req = request.form
    if controller.deleteUser(req['email']):
        return redirect('/accountDeleted')
    else:
        return render_template('account_error.html')


@app.route('/accountDeleted')
def accountDeleted():
    return render_template('account_deleted.html')


@app.route('/allAccounts')
def allAccounts():
    return controller.getAll()
#
# @login_manager.user_loader()
# def user_loader(user_id):
#     return controller.findUserByID(user_id)
