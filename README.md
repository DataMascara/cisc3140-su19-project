# CISC 3140 - Summer 2019 Project
This is the repository for the group project in CISC 3140 class at Brooklyn College.

## UnderDogs

UnderDogs is an information hub for Brooklyn College Computer Science students and faculty. Users can share original content, ask for assistance from other students, find collaborators, and have discussions across an array of curated communities.

## Team-Specific ReadMe
- [Product Team README](https://github.com/DataMascara/cisc3140-su19-project/blob/master/product/README.md)
- Backend
- ect.

# Setup

## Installation

Base-requirements: 
- Python3, 
- Flask Web Framework

## Installing dependencies from the `requirements.txt` file.

- To install dependencies from the `requirements.txt` file: 
```pip3 install -r requirements.txt```
- When new Python libraries are required, update the `requirements.txt` file using the command and push the file to Github. (or `pip` instead of `pip3`
```pip3 freeze > requirements.txt```

## Running

- **NOTE:** MinimalAPI functionality is currently implemented, with no VIEW/connecting link to the front end.
- Alpha release will be served on a server soon so that features can be continuously implemented
- Navigate to the `app/` folder and execute `python app.py` or `python3 app.py` (depending on your setup)


## Signing Up

Firstly, make sure that UnderDogs website is running in your web browser.
- Open the tab on the left side of the browser

## Signing In

First, make sure you have the API running and you note down the url ie `localhost:8080`
- Open the tab on the left and enter the following information into the fields:
- Username: `username`
- Password: `password`
``` 
{
  "users": [
    {
      "avatarUrl": null,
      "dateCreated": "2019-07-25 23:46:14",
      "dateModified": null,
      "email": "chalshaff12@gmail.com",
      "first": "Michal",
      "isActive": 1,
      "last": "Shaffer",
      "password": "hashedpassword",
      "userid": 246815,
      "username": "chalshaff12"
    }
  ]
}
```

### Test on a user that doesn't exist

- Follow the above steps but put `{"user":"notrealuser13"}` into the raw body (notrealuser13 does NOT exist, so you should get a response that indicates that) - TADA! You should see `{"error": "User Not found!"}` in the response body below with a status of 404!
