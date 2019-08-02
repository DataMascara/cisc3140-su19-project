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
	column = request.args.get('column')
	value = request.args.get('value')
	#calling the select statement function
	resultSet = dbmodule.findUsers(column, value)
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
	avatarurl = request.args.get('avatarurl')
	description = request.args.get('description')

	#calling the insert statement function
	resultSet = dbmodule.insertUser(email, password, username, first, last, avatarurl, description)
	return str(resultSet)


#add a user with http://localhost:5000/addUser?email=[email]&password=[password]&username=[username]&first=[first]&last=[last]
@app.route('/deleteUser')
def deleteUser():
	#getting parameters and setting variables
	username = request.args.get('username')
	#calling the insert statement function
	resultSet = dbmodule.deleteUser(username)
	return str(resultSet)

#get all posts  by port name
#input portname (String)
#output tbd
@app.route('/allPostsbyPort')
def allPostsbyPort():
	portName = request.args.get('portName')
	resultSet = dbmodule.allPostsbyPort(portName)
	return str(resultSet)