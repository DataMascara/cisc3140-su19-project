import mysql.connector
import json
import datetime


def dbconnection():
    # localhost
    # mydb = mysql.connector.connect(
    # 		host="localhost",
    # 		user="root",
    # 		passwd="",
    # 		database="dbtest"
    # )

    # webhosteddb
    mydb = mysql.connector.connect(
        host="35.239.141.59",
        user="backendteam",
        passwd="UZSDmp7J2J2ZYHw",
        # test db
        database="test_db"
        # deploymentdb
        #   database="cisc3140"
    )

    return mydb


class subscriptions_db:
    # by username, portname, or portid

    # The function all_subscriptions_by has the inputs column_name (string)
    # It also takes in the data_value (int?)
    # Output: the column names that are equal to the search query
    # ex:

    def all_subscriptions_by(column_name, data_value):

        mydb = dbconnection()
        # create db cursor
        cursor = mydb.cursor(buffered=True)
        # sql statement
        sql = f"SELECT * FROM subscriptions_vw WHERE {column_name} = '{data_value}'"

        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        result_set = cursor.fetchall()  # save sql result set
        # convert columns and rows into json data
        json_data = [dict(zip([key[0] for key in cursor.description], row)) for row in result_set]
        # close database connection

        cursor.close()
        mydb.close()

        # catch datetime datatype error for json
        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return json.dumps({'all_subscriptions for {data_value}': json_data}, default=myconverter)

    # input: email (string), password (hashed string), username (string), first (String), last (string),
    # description (string), avatarUrl (string)
    # email and username must be unique (use find_user)
    # password should be hashed
    # ALL fields are REQUIRED!!

    # the output of this functions should return the username and their portid number
    def add_subscription(username, port_id):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)

        sql = f"INSERT INTO subscriptions (userId, portId) VALUES ((SELECT id FROM users WHERE username = '{username}'), {port_id})"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return all_subscriptions('portId', portId)

    # input: username (string)
    # returns: if subscription is active
    # the username, and their port_id number
    def update_subscription(username, port_id, value):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)

        sql = f"UPDATE subscriptions SET isActive = {value} WHERE userId = (SELECT id FROM users WHERE username = '{username}') and portId = {port_id}"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return f"subscription {username} to port {port_id} is updated"


class ports_db:

    # No input
    # returns the id, name and description if the port is open
    def all_ports_by(self):

        mydb = dbconnection()
        # create db cursor
        cursor = mydb.cursor(buffered=True)
        # sql statement
        sql = '''SELECT id, name, description FROM ports where isActive = 1'''

        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        result_set = cursor.fetchall()  # save sql result set
        # convert columns and rows into json data
        json_data = [dict(zip([key[0] for key in cursor.description], row)) for row in result_set]
        # close database connection

        cursor.close()
        mydb.close()

        # catch datetime datatype error for json
        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return json.dumps({'all_ports': json_data}, default=myconverter)

    def add_port(name, description):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"INSERT INTO ports (name, description) VALUES ('{name}', '{description}')"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return posts_db.all_ports()


class users_db:

    # no input, returns all active users
    # returns fields: userid, username, email, first, last, avatarUrl

    def all_users():

        mydb = dbconnection()
        # create db cursor
        cursor = mydb.cursor(buffered=True)
        # sql statement
        sql = '''SELECT * FROM users_vw'''

        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        result_set = cursor.fetchall()  # save sql result set
        # convert columns and rows into json data
        json_data = [dict(zip([key[0] for key in cursor.description], row)) for row in result_set]
        # close database connection

        cursor.close()
        mydb.close()

        # catch datetime datatype error for json
        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return json.dumps({'all_users': json_data}, default=myconverter)

    # input: column_name (string), data_value (string or int)
    # options and types:
    # column_name: data_value
    # user_id: int
    # username: string
    # email: string
    # output: userid, username, email, first, last, avatarUrl
    # e.g. http://localhost:5000/find_users?column=username&value=chalshaff12
    # or http://localhost:5000/find_users?column=email&value=chalshaff12@gmail.com
    def find_users(column_name, data_value):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)

        sql = f"SELECT * FROM users_vw WHERE {column_name} = '{data_value}'"

        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        result_set = cursor.fetchall()  # save sql result set
        # convert columns and rows into json data
        json_data = [dict(zip([key[0] for key in cursor.description], row)) for row in result_set]

        # close database connection
        cursor.close()
        mydb.close()

        # catch datetime datatype error for json
        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return json.dumps({'user': json_data}, default=myconverter)

    # input: email (string), password (hashed string), username (string), first (String), last (string), description (string), avatarUrl (string)
    # email and username must be unique (use find_user)
    # password should be hashed
    # all fields are required!!
    def add_user(email, password, username, first, last, avatarurl):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)

        sql = f"INSERT INTO users (email, password, username, first, last, description, avatarurl) VALUES ('{email}','{password}','{username}','{first}','{last}', '{description}', '{avatarurl}')"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return find_users('username', username)

    # input: username (string), column_name(string?), value_name(string?)
    # output: it displays the 'username': changed_username

    def update_user(username, column_name, value_name):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)

        sql = f"UPDATE users SET {column_name} = '{value_name}' WHERE username = '{username}'"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return find_users('username', username)

    # input: username (string)

    # The function delete_user takes in the username(string) as the input
    # returns: user is deleted

    def delete_user(username):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)

        sql = f"UPDATE users SET isActive = 0 WHERE username = '{username}'"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return f"user {username} deleted"


class posts_db:

    # column_name = port_id or author
    # data_value depends on the column (always a string)
    # e.g. http://localhost:5000/all_posts_by?column=author&value=chalshaff12
    # or http://localhost:5000/all_posts_by?column=port_id&value=1
    def all_posts_by(column_name, data_value):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"SELECT * FROM posts_vw where {column_name} = '{data_value}'"

        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        result_set = cursor.fetchall()  # save sql result set
        # convert columns and rows into json data
        json_data = [dict(zip([key[0] for key in cursor.description], row)) for row in result_set]
        # close database connection

        cursor.close()
        mydb.close()

        # catch datetime datatype error for json
        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return json.dumps({'posts': json_data}, default=myconverter)

    # input: add_post takes in title(varchar) text(text) port_id(int) author(string)

    # output: it returns the title and the author

    def add_post(title, text, port_id, author):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"INSERT INTO posts (title, text, portid, userid) VALUES ('{title}','{text}',{port_id}, (select id from users where username = '{author}'))"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return posts_db.all_posts_by('author', author)

    # delete_post takes in the input post_id(int)
    # if deleted the boolean value is set to 1 it
    # returns that the post [post_id] was deleted

    def delete_post(post_id):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"UPDATE posts SET isDeleted = 1 WHERE id = {post_id}"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return f"post {post_id} deleted"

    # update_post function has the input post_id(int), column_name(string), data_value(int)
    # returns all the posts by the author and the authors post_id

    def update_post(post_id, column_name, data_value):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"UPDATE posts SET {column_name} = '{data_value}' where id = {post_id}"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return posts_db.all_posts_by('author', post_id)


class comments_db:

    # input is column_name(string) and data_value(int?)

    # returns:

    def all_comments_by(column_name, data_value):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"SELECT * FROM comments_vw where {column_name} = '{data_value}'"

        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        result_set = cursor.fetchall()  # save sql result set
        # convert columns and rows into json data
        json_data = [dict(zip([key[0] for key in cursor.description], row)) for row in result_set]
        # close database connection

        cursor.close()
        mydb.close()

        # catch datetime datatype error for json
        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return json.dumps({'comments': json_data}, default=myconverter)

    # input text(text), post_id(int), parent_id(int), author(string)

    # returns the post_id and the author

    def add_comment(text, post_id, parent_id, author):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"INSERT INTO comments ('{text}', {post_id}, {parent_id}, (select id from users where username = '{author}'))"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return posts_db.all_comments('author', author)

    # input comment_id(int)

    # returns that the comment is deleted

    def delete_comment(comment_id):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"UPDATE comments SET isDeleted = 1 WHERE id = {comment_id}"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return f"comment {comment_id} deleted"

    # input comment_id(int) and text(text)

    # returns the text and column_id

    def update_comment(comment_id, text):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"UPDATE comments SET text = '{text}' where id = {comment_id}"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return posts_db.all_comments_by('comment_id', comment_id)


class votes_db:

    # type = 'post' or 'comment'
    # column_name = 'saved' or 'vote'
    # data_value = '1' for saved, '1' for upvotes, '-1' for downvotes

    # this functions takes the user_id, column_name, data_value and type
    # output: it returns the text, author, the username of who votes, the vote[-1,0,1]
    # and wether it is comment or post

    def all_votes_by(user_id, column_name, data_value, type):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"SELECT * FROM votes_vw where userId = {user_id} and {column_name} = '{data_value}' and type = '{type}'"

        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        result_set = cursor.fetchall()  # save sql result set
        # convert columns and rows into json data
        json_data = [dict(zip([key[0] for key in cursor.description], row)) for row in result_set]
        # close database connection

        cursor.close()
        mydb.close()

        # catch datetime datatype error for json
        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return json.dumps({'voted_data': json_data}, default=myconverter)

    # saved = 1 or 0
    # vote = -1, 0 or 1
    # type = 'post' or 'comment'
    # item_id = the post or comment ID
    # if saving the post or comment, set vote = 0 or null.

    # this functions takes the input: user_id, item_id, save, vote and type
    # output: gives you the table all_votes_by and returns the user_id

    def add_vote(user_id, item_id, save, vote, type):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"INSERT INTO votes (userid, post_id, isSaved, vote, type) VALUES ({user_id}, {item_id}, {save}, {vote}, {type}))"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return posts_db.all_votes_by('userId', user_id)

    # if it is a post, put null for comment_id
    # if it is a comment, put null for post_id
    # column_name = 'isSaved' or 'vote'
    # data_value = 1 or 0 for 'isSaved', 1,0,-1 for 'vote'

    # this function takes the inputs user_id, post_id, comment_id, column_name and data_value
    # the output returns that the vote is updated

    def update_vote(user_id, post_id, comment_id, column_name, data_value):

        mydb = dbconnection()
        cursor = mydb.cursor(buffered=True)
        sql = f"UPDATE votes SET {column_name} = {data_value} WHERE user_id = {user_id} and post_id = {post_id} or comment_id = {comment_id}"

        try:
            cursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as err:
            return json.dumps({'error': str(err)})

        # close database connection
        cursor.close()
        mydb.close()

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        return f"vote updated"

