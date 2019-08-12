from app import app, dbmodule
import requests
from flask import request 

#index/home page
@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"
	

@app.route('/allPorts')
def all_ports():
	#calling the select statement function
	result_set = dbmodule.ports_db.all_ports()
	return str(result_set)

@app.route('/addPort')
def add_port():
	#getting parameters and setting variables
	name = request.args.get('name')
	description = request.args.get('description')
	#calling the insert statement function
	result_set = dbmodule.ports_Db.add_port(name, description)
	return str(result_set)

#select all users with http://localhost:5000/all_users
@app.route('/allUsers')
def all_users():
	#calling the select statement function
	result_set = dbmodule.users_db.all_users()
	return str(result_set)

#find users by username with http://localhost:5000/all_users?username=[insert username to search for]
@app.route('/findUsers')
def find_users():
	#get parameter and set variable
	column = request.args.get('column')
	value = request.args.get('value')
	#calling the select statement function
	result_set = dbmodule.users_db.find_users(column, value)
	return result_set

#add a user with http://localhost:5000/addUser?email=[email]&password=[password]&username=[username]&first=[first]&last=[last]
@app.route('/addUser')
def addUser():
	#getting parameters and setting variables
	email = request.args.get('email')
	password = request.args.get('password')
	username = request.args.get('username')
	first = request.args.get('first')
	last = request.args.get('last')
	description = request.args.get('description')
	avatarurl = request.args.get('avatarurl')
	#calling the insert statement function
	result_set = dbmodule.users_db.add_user(email, password, username, first, last, description, avatarurl)
	return str(result_set)

@app.route('/updateUser')
def update_user():
	#getting parameters and setting variables
	username = request.args.get('username')
	column = request.args.get('column')
	value = request.args.get('value')
	
	#calling the insert statement function
	result_set = dbmodule.users_db.update_user(username, column, value)
	return str(result_set)

#add a user with http://localhost:5000/addUser?email=[email]&password=[password]&username=[username]&first=[first]&last=[last]
@app.route('/deleteUser')
def delete_user():
	#getting parameters and setting variables
	username = request.args.get('username')
	#calling the insert statement function
	result_set = dbmodule.delete_user(username)
	return str(result_set)

@app.route('/allPostsBy')
def all_posts_by():
	column = request.args.get('column')
	value = request.args.get('value')
	result_set = dbmodule.posts_db.all_posts_by(column, value)
	return str(result_set)


@app.route('/addPost')
def add_post():
	#getting parameters and setting variables
	title = request.args.get('title')
	text = request.args.get('text')
	author = request.args.get('author')
	port_name = request.args.get('port_name')
	image = request.args.get('image')

	#calling the insert statement function
	result_set = dbmodule.posts_db.add_post(title, text, port_name, author, image)
	return str(result_set)

@app.route('/deletePost')
def delete_post():
	#getting parameters and setting variables
	post_id = request.args.get('post_id')
	#calling the insert statement function
	result_set = dbmodule.posts_db.delete_post(post_id)
	return str(result_set)


@app.route('/updatePost')
def update_post():
	#getting parameters and setting variables
	post_id = request.args.get('post_id')
	column = request.args.get('column')
	value = request.args.get('value')
	
	#calling the insert statement function
	result_set = dbmodule.posts_db.update_post(post_id, column, value)
	return str(result_set)

@app.route('/allCommentsBy')
def all_comments_by():
	column = request.args.get('column')
	value = request.args.get('value')
	result_set = dbmodule.comments_db.all_comments_by(column, value)
	return str(result_set)


@app.route('/addComment')
def add_comment():
	#getting parameters and setting variables
	text = request.args.get('text')
	author = request.args.get('author')
	post_id = request.args.get('post_id')
	parent_id = request.args.get('parent_id')
	
	#calling the insert statement function
	result_set = dbmodule.comments_db.add_comment(text, post_id, parent_id, author)
	return str(result_set)

@app.route('/deleteComment')
def delete_comment():
	#getting parameters and setting variables
	_comment_id = request.args.get('comment_id')
	#calling the insert statement function
	result_set = dbmodule._comment_db.delete_comment(_comment_id)
	return str(result_set)


@app.route('/updateComment')
def update_comment():
	#getting parameters and setting variables
	comment_id = request.args.get('comment_id')
	text = request.args.get('text')
	
	#calling the insert statement function
	result_set = dbmodule.comments_db.update_comment(comment_id, text)
	return str(result_set)


@app.route('/allSubscriptionsBy')
def all_subscriptions_by():
	column = request.args.get('column')
	value = request.args.get('value')
	result_set = dbmodule.subscriptions_db.all_subscriptions_by(column, value)
	return str(result_set)


@app.route('/addSubscription')
def add_subscription():
	#getting parameters and setting variables
	username = request.args.get('username')
	port_id = request.args.get('port_id')
	
	#calling the insert statement function
	result_set = dbmodule.comments_db.subscriptions_db(username, port_id)
	return str(result_set)

@app.route('/updateSubscription')
def update_subscription():
	#getting parameters and setting variables
	username = request.args.get('username')
	port_id = request.args.get('port_id')
	value = request.args.get('value')
	#calling the insert statement function
	result_set = dbmodule.subscriptions_db.update_subscription(username, portId, value)
	return str(result_set)

@app.route('/allVotesBy')
def all_votes_by():
	username = request.args.get('username')
	column = request.args.get('column')
	value = request.args.get('value')
	type = request.args.get('type')
	operation = request.args.get('operation')
	result_set = dbmodule.votes_db.all_votes_by(username, column, value, type, operation)
	return str(result_set)
