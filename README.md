## Back-end Barebones Branch has a Barebones REST, CRUD (Create, Read, Update, Delete) API

- Currently uses a minimal flask module `database.py` which makes a connection to a remote database

  - `main.py` imports and uses the one function currently described in the `database` module.

## Dependencies

Install dependencies from the `requirements.txt` file.
`pip3 install -r requirements.txt`

- If you're having trouble installing flask mysql go to [https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
  and download your respective mysqlcleint.whl file (ie `mysqlclient‑1.4.2‑cp37‑cp37m‑win32.whl` is for python 3.7 on windows,) The numbers following cp are the version of python, so cp37 if you're using python 3.7. then `pip install <PATH TO THE .whl FILE>` and you should be able to `pip install flask-mysqldb` - For more info on flask mysql check out the docs at [https://flask-mysqldb.readthedocs.io/en/latest/](https://flask-mysqldb.readthedocs.io/en/latest/)

## Running

Navigate to the `app/` folder and execute `python main.py` or `python3 main.py` (depending on your setup)
Use postman ([https://www.getpostman.com/](https://www.getpostman.com/)) to test the API.
Debug user that already exists is :Mike1234 (it returns his password haha)

## Try a GET Request

First, make sure you have the API running and you note down the url ie `127.0.0.0:5000`

- Open Postman and go to the header tab and your header Content-Type to "application/json"
- Go to the "Body" tab and check the "raw" and "JSON(application/json) options under that tab
- Now put `{"user":"mike1234"}` into the raw body (mike1234 exists, so you should get a response that indicates that)
- Set the request to GET and the URL `http://YOURLOCALHOSTURL:5000/user` - TADA! You should see `{"msg": "User found!"}` in the response body below with a status of 200!

### Test on a user that doesn not exist

- Follow the above steps but put `{"user":"notrealuser13"}` into the raw body (notrealuser13 does NOT exist, so you should get a response that indicates that) - TADA! You should see `{"error": "User Not found!"}` in the response body below with a status of 404!

# Handling json and python dictionaries

If you're processing a request in flask (hopefully using the request import), you'll need a way to turn a json request into a python readable form. Additionally, you're

## Handling an incoming json response

A good way to do this is to take your request and invoke the `.get_json()` method on request. This goes into the request and "parses-out" the data from the json into python ready code! One important thing to note is that the content type header and form of the json must already be valid, otherwise a error will be thrown. Using flask request already does this for us, but it's important to keep in mind.

See the example code below

```
from flask import Flask, request, render_template_string
...
@app.route('/takejson',methods=["POST"])
def takejson():	#Let's say we sent the following json: {"name":"Anton"}
    data = request.get_json() #The data var is now a python dictionary with the json values!
    return render_template_string('hello {{ what }}', what=data["name"])
    #Return the data that we pulled out and expect!
```

## Sending a JSON response

After we have handled data, or done whatever was needed, we're going to want our API to send a response in JSON form so that our API can talk to any(almost) interface. A simple way to do this is to use flask's jsonify module that returns a flask.Response() object that does some of the grunt work for us (setting the header's content type to application/json and so on) vs using alternative methods like json.dumps() which simply attempts to converted to json string.

Let's take a look at an example below

```
from flask import Flask, request, jsonify
...
@app.route('/takejson',methods=["GET"])
def takejson():	#Let's say we sent the following json: {"name":"Anton"}
    data = {"Is the earth flat?":"Maybe"} # Make a python dict (could have been generated from the user)    return render_template_string('hello {{ what }}', what=data["name"])
    return jsonify(data) #Return a valid-form json as a flask.Response object.
```

Try this out using a API interface such as Postman!

# Going between json and python dictionaries

## Use the `json.loads()` method to load a python string that is valid JSON into a python dictionary

Given:

```
#Python string that is valid json
str_json= '''{
	"users": ["appMan", "CSMajor1993", null, "leetc0der1337"]
	}'''
data = json.loads(str_json) #Passing the string into the load s turns the json string into a python dict!
#Parses null into None, Json array to lists and so on.

print(data) # Prints the now dictionary
users_list = data['users']
# We can loop through the users by using the key to get the list
for username in users_list:
	print(username)
```

## Use the `json.dumps()` to dump a python object to a JSON-valid string

If we wanted to edit the python dictionary we now have from the json, we can simply `del` to delete a key and value pair, or remove it from the list.
Given:

```

print(data)
# Replace the list with an updated list in the dict
data['users'] = [username for username in users_list if (username !=  'appMan')]
print(data)
# Make a new json string from our now modified dictionary
updated_json_string = json.dumps(data, indent=2) #2nd param allows sort_keys and style the json-string

# Note the conversion from null to None back to null!
print(updated_json_string)
```

# Running your app in debug mode using the flask CLI

    If you're setting FLASK_DEBUG=1, and working in a virtual env you may find a infamous `Restarting with stat` issue.
    To work around this issue run `python -m flask run`. This seems to be an odd issue with the -m / module invocation falling off when using the debugger.
