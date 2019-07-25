import mysql.connector
import json
import datetime


def allUsers():	
	#create db connection
	mydb = mysql.connector.connect(
		host="35.239.141.59",
		user="backendteam",
		passwd="UZSDmp7J2J2ZYHw",
		database="test_db"
	)
	#create db cursor
	cursor = mydb.cursor(buffered=True)
	#sql statement
	sql = '''SELECT * FROM users;'''
	#execute sql statement
	cursor.execute(sql)
	#save sql result set
	resultSet = cursor.fetchall()	
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


def findUsers(usernameValue):
	mydb = mysql.connector.connect(
		host="35.239.141.59",
		user="backendteam",
		passwd="UZSDmp7J2J2ZYHw",
		database="test_db"
	)
	cursor = mydb.cursor(buffered=True)
	#if len(userID) > 0:
	column = 'username'
	value = usernameValue
	#elif len(username) > 0:
	#else:
	#	column = 'email'
	#	value = email
	sql = f"SELECT * FROM users WHERE {column} = '{value}'"
	cursor.execute(sql)
	#num_fields = len(cursor.description)
	#columns = [i[0] for i in cursor.description]
	resultSet = cursor.fetchall()
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


#email and username should be unique
#password should be hashed
#all fields are required!!
def insertUser(email, password, username, first, last):
	mydb = mysql.connector.connect(
		host="35.239.141.59",
		user="backendteam",
		passwd="UZSDmp7J2J2ZYHw",
		database="test_db"
	)
	cursor = mydb.cursor(buffered=True)
	sql = f"INSERT INTO users (email, password, username, first, last) VALUES ('{email}','{password}','{username}','{first}','{last}')"
	cursor.execute(sql)
	mydb.commit()
	resultSet=allUsers()
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



