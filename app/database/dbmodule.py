import mysql.connector
import json
import datetime

def dbconnection():

	#localhost
	# mydb = mysql.connector.connect(
	# 		host="localhost",
	# 		user="root",
	# 		passwd="",
	# 		database="dbtest"
	# )


	#webhosteddb
	mydb = mysql.connector.connect(
		host="35.239.141.59",
		user="backendteam",
		passwd="UZSDmp7J2J2ZYHw",
	#test db
		database="test_db"
	#deploymentdb
	#   database="cisc3140"
	)

	return mydb


#no input, returns all active users
#returns fields: userid, username, email, first, last, avatarUrl
def allUsers():	

	mydb = dbconnection()
	#create db cursor
	cursor = mydb.cursor(buffered=True)
	#sql statement
	sql = '''SELECT * FROM users where isActive = 1'''

	try:
		cursor.execute(sql)
	except mysql.connector.Error as err:
		return json.dumps({'error':str(err)})

	resultSet = cursor.fetchall()		#save sql result set
	#convert columns and rows into json data
	jsonData = [dict(zip([key[0] for key in cursor.description], row)) for row in resultSet]
	#close database connection

	cursor.close()
	mydb.close()

	#catch datetime datatype error for json
	def myconverter(o):
		if isinstance(o, datetime.datetime):
			return o.__str__()
	return json.dumps({'users':jsonData}, default = myconverter)


#input: columnValue (string), valueValue (string or int) 
#options and types:
#columnValue: valueValue
#userId: int
#username: string
#email: string
#output: userid, username, email, first, last, avatarUrl
def findUsers(columnValue, valueValue):

	mydb = dbconnection()
	cursor = mydb.cursor(buffered=True)

	sql = f"SELECT * FROM users WHERE {columnValue} = '{valueValue}' and isActive = 1"
	
	try:
		cursor.execute(sql)
	except mysql.connector.Error as err:
		return json.dumps({'error':str(err)})
	
	resultSet = cursor.fetchall()		#save sql result set
	#convert columns and rows into json data
	jsonData = [dict(zip([key[0] for key in cursor.description], row)) for row in resultSet]

	#close database connection
	cursor.close()
	mydb.close()
	#catch datetime datatype error for json
	def myconverter(o):
		if isinstance(o, datetime.datetime):
			return o.__str__()

	return json.dumps({'users':jsonData}, default = myconverter)


#input: email (string), password (hashed string), username (string), first (String), last (string), avatarUrl (string)
#email and username must be unique (use findUser)
#password should be hashed
#all fields are required!!
def insertUser(email, password, username, first, last, avatarurl):

	mydb = dbconnection()
	cursor = mydb.cursor(buffered=True)

	sql = f"INSERT INTO users (email, password, username, first, last, avatarurl) VALUES ('{email}','{password}','{username}','{first}','{last}','{avatarurl}')"
	
	try:
		cursor.execute(sql)
		mydb.commit()
	except mysql.connector.Error as err:
		return json.dumps({'error':str(err)})

	#close database connection
	cursor.close()
	mydb.close()
	
	def myconverter(o):
		if isinstance(o, datetime.datetime):
			return o.__str__()

	return findUsers('username', username)



#input: username (string)
def deleteUser(username):

	mydb = dbconnection()
	cursor = mydb.cursor(buffered=True)

	sql = f"UPDATE users SET isActive = 0 WHERE username = '{username}'"
	
	try:
		cursor.execute(sql)
		mydb.commit()
	except mysql.connector.Error as err:
		return json.dumps({'error':str(err)})
	
	#close database connection
	cursor.close()
	mydb.close()
		
	def myconverter(o):
		if isinstance(o, datetime.datetime):
			return o.__str__()

	return f"user {username} deleted"
	

def showPortPosts(portName):

	mydb = dbconnection()
	cursor = mydb.cursor(buffered=True)

	sql=  f"select p.posttext, u.username as author, v.vote as votes from posts p left join users u on p.userid = u.userid left join votes v on v.postid = p.postid where p.isDeleted = 0 and p.portid = (select portid from ports where portname = '{portName}')"

	try:
		cursor.execute(sql)
	except mysql.connector.Error as err:
		return json.dumps({'error':str(err)})

	resultSet = cursor.fetchall()		#save sql result set
	#convert columns and rows into json data
	jsonData = [dict(zip([key[0] for key in cursor.description], row)) for row in resultSet]
	#close database connection

	cursor.close()
	mydb.close()

	#catch datetime datatype error for json
	def myconverter(o):
		if isinstance(o, datetime.datetime):
			return o.__str__()
	return json.dumps({'posts':jsonData}, default = myconverter)	
	
