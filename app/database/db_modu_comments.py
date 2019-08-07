# The function insertUser takes in the ***input***:
# 1. Email(String)
# 2. Password(hashed string)
# 3. usernme(string)
# 4. first(string)
# 5. last(string)
# 6. avatarURL(string)
#
#
# * ***Email and Username MUST be unique***
# * ***EVERY*** feild is *required*

def insertUser(email, password, username, first, last, avatarurl, description):


mydb = dbconnection()

cursor = mydb.cursor(buffered=True)

sql = f"INSERT INTO users (email, password, username, first, last, avatarurl, description) VALUES ('{email}','{password}','{username}','{first}','{last}','{avatarurl}',{description})"

try:

cursor.execute(sql)

mydb.commit()

except mysql.connector.Error as err:

return json.dumps({'error': str(err)})

# close database connection

cursor.close()

mydb.close()

# ----------------------------------------------

# The function deleteUser takes in the **input**:
# 1. *username* feild which is a *string* as the parameter
# 2. The output returns that the -username is deleted

def deleteUser(username):



mydb = dbconnection()

cursor = mydb.cursor(buffered=True)



sql = f"UPDATE users SET isActive = 0 WHERE username = '{username}'"


#close database connection

cursor.close()

mydb.close()

return f"user {username} deleted"

# The function findUsers takes **input**:
#
# 1. The columnValue (string) is the column for what youre searching for
#     * columnValue can take in the id, username or email columns
# 2. valueValue (string or int) id (int) or username(string)
# 3. Email (string)
#
# (username, id, email) columnValue = valueValue (actual values such as emails, id numbers)
#
# columnValue = 'username'
#
# columnValue = 'username'
# valueValue = 'alina_kay'
#
# **OR**
#
# columnValue = 'id'
# valueValue = 31
#
# **OR**
#
# columnValue = 'email'
# valueValue = alina_kay@email.com
#
#
# - Value is what you are searching for from these three feilds in the table
#
#
# The *output* displays the userid, username, email, first, last, avatarUrl


def findUsers(columnValue, valueValue):



mydb = dbconnection()

cursor = mydb.cursor(buffered=True)



sql = f"SELECT * FROM users WHERE {columnValue} = '{valueValue}' and isActive = 1"



try:

cursor.execute(sql)

except mysql.connector.Error as err:

return json.dumps({'error':str(err)})



resultSet = cursor.fetchall() #save sql result set

#convert columns and rows into json data

jsonData = [dict(zip([key[0] for key in cursor.description], row)) for row in resultSet]



#close database connection

cursor.close()

mydb.close()


#The function showPortPosts takes in the parameter portName(varChar)


def showPortPosts(portName):



mydb = dbconnection()

cursor = mydb.cursor(buffered=True)



sql= f"select p.text, u.username as author, v.vote as votes from posts p left join users u on p.userid = u.id left join votes v on v.postid = p.id where p.isDeleted = 0 and p.portid = (select id from ports where name = '{portName}')"




cursor.close()

mydb.close()



#catch datetime datatype error for json
