from app import app, dbmodule
import requests
from flask import request
from dbmodule import add_port,find_users,add_user,update_user,delete_user,add_post,delete_post

def testport():
	assert(add_port(StevenGinsberg,student)== str(resultset))

	def test all_users():
	assert(all_users(StevenGinsberg,student)== str(resultset))
def test find_users():
	assert(find_users(StevenGinsberg,student)== str(resultset))
def test add_user():
	assert(add_user(StevenGinsberg,student)== str(resultset))
def test update_user():
	assert(update_user(StevenGinsberg,student)== str(resultset))
def test delete_user():
	assert(delete_user(StevenGinsberg,student)== str(resultset))
def  test add_post():
	assert(add_post('Chocolate chip Cookies','Yum Yum Yum','StevenGinsberg','portid')== str(resultset))

def  test delete_post():
	assert(delete_post(post_id)== str(resultset))
