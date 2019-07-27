# cisc3140-su19-project

This is the repository for the group project in CISC 3140 class at Brooklyn College.

# Setup

## Installation
Base-requirements: Python3, Flask Web Framework


## Installing dependencies from the `requirements.txt` file. 
To install dependencies from the `requirements.txt` file.
`pip3 install -r requirements.txt`
When new Python libraries are required, update the `requirements.txt` file using the command.
`pip3 freeze > requirements.txt` and push the file to Github. (or `pip` instead of `pip3`

## Running
Navigate to the `app/` folder and execute `python main.py` or `python3 main.py` (depending on your setup)
Use postman ([https://www.getpostman.com/](https://www.getpostman.com/)) to test the API.
Debug user that already exists is :chalshaff12 (it returns his password)
 	- Currently, the API is just working in some cases and not linked to a view page yet
	- Server hoasting for live demo is coming soon.

## Try a GET Request

First, make sure you have the API running and you note down the url ie `127.0.0.0:5000`

- Open Postman and go to the header tab and your header Content-Type to "application/json"
- Go to the "Body" tab and check the "raw" and "JSON(application/json) options under that tab
- Now put `{"user":"mike1234"}` into the raw body (if mike1234 exists, so you should get a response that indicates that)
- Set the request to GET and the URL `http://YOURLOCALHOSTURL:5000/user` - TADA! You should see `{"msg": "User found!"}` in the response body below with a status of 200!

### Test on a user that doesn not exist

- Follow the above steps but put `{"user":"notrealuser13"}` into the raw body (notrealuser13 does NOT exist, so you should get a response that indicates that) - TADA! You should see `{"error": "User Not found!"}` in the response body below with a status of 404!



