from app import app, dbmodule
import requests
from flask import request 

#index/home page
@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"
	
#select all users with http://localhost:5000/allUsers
@app.route('/allUsers')
def allUsers():
	#calling the select statement function
	resultSet = dbmodule.allUsers()
	return str(resultSet)

#find users by username with http://localhost:5000/allUsers?username=[insert username to search for]
@app.route('/findUsers')
def findUsers():
	#get parameter and set variable
	username = request.args.get('username')
	#calling the select statement function
	resultSet = dbmodule.findUsers(username)
	return resultSet

#add a user with http://localhost:5000/addUser?email=[email]&password=[password]&username=[username]&first=[first]&last=[last]
@app.route('/addUser')
def addUser():
	#getting parameters and setting variables
	email = request.args.get('email')
	password = request.args.get('password')
	username = request.args.get('username')
	first = request.args.get('first')
	last = request.args.get('last')
	#calling the insert statement function
	resultSet = dbmodule.insertUser(email, password, username, first, last)
	return str(resultSet)