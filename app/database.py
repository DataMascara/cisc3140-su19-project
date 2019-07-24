from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql9299677'
app.config['MYSQL_PASSWORD'] = 'NpxJDZNdlX'
app.config['MYSQL_DB'] = 'sql9299677'
mysql = MySQL(app)


def get_user(username):
    cur = mysql.connection.cursor()
    command_str = '''SELECT password FROM users WHERE username = '{}' '''
    new = command_str.format(username)
    print(new)
    cur.execute(new)
    rv = cur.fetchall()
    return str(rv)
    


if __name__ == '__main__':
    app.run(debug=True)
