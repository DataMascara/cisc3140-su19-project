import mysql.connector
import json
import datetime

stored_proc = {

    'users': {

        'getallusers': '''SELECT * FROM users;''',
        'getuser': '''SELECT * FROM users WHERE username='''

    }

}


def build_query(query, options):

    return stored_proc['users'][query] + options


def connect():

    # create db connection
    mydb = mysql.connector.connect(
        host="35.239.141.59",
        user="backendteam",
        passwd="UZSDmp7J2J2ZYHw",
        database="test_db"
    )

    return mydb


def query_to_json(query):

    mydb = connect()

    # create db cursor
    cursor = mydb.cursor(buffered=True)
    # sql statement
    sql = query
    # execute sql statement
    cursor.execute(sql)
    # save sql result set
    resultSet = cursor.fetchall()
    # convert columns and rows into json data
    jsonData = [dict(zip([key[0] for key in cursor.description], row))
                for row in resultSet]
    # close database connection
    cursor.close()
    mydb.close()
    # catch datetime datatype error for json

    def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()
    return json.dumps({'users': jsonData}, default=myconverter)


def test():
    return query_to_json(build_query('getallusers', ''))
