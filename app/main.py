from flask import Flask, render_template, request, redirect, jsonify
import requests
import os
import json
from database import get_user
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql9299677'
app.config['MYSQL_PASSWORD'] = 'NpxJDZNdlX'
app.config['MYSQL_DB'] = 'sql9299677'
mysql = MySQL(app)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        res = request.form
        # Grab the user and pw
        user = res['username']
        # password = res['password']
        # If db.validate_user_cred
        # return jsonify({"msg": "login success"}), 200
        # return jsonify({"error": "Credentials Not Valid!"})
        return get_user(user)
    return get_user(user)


@app.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if(request.method == 'POST'):
        res = request.form  # Grab the form
        email = res['email']
        user = res['username']
        password = res['password']
        # if(validate_user(users_db, user)):
        #     return jsonify({"error": "User Already Registered"})
        # Signal DB Of new record
        return jsonify({"msg": "User Added"})
    return jsonify({"msg": "User Already Exists"})


@app.route('/delete', methods=['POST', 'GET'])
def test():
    if(request.method == 'POST'):
        res = request.get_json()  # Grab the response as a python dict
        print(type(res))
        user = res['user'].lower()
        print(user)
        return jsonify({"msg": "no result"})


if(__name__ == "__main__"):
    app.run(debug=True)
