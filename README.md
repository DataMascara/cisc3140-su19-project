# CISC 3140 - Summer 2019 Project [![Build Status](https://travis-ci.org/DataMascara/cisc3140-su19-project.svg?branch=master)](https://travis-ci.org/DataMascara/cisc3140-su19-project)
This is the repository for the group project in CISC 3140 Summer Session 2 2019 class at Brooklyn College.

## UnderDogs
UnderDogs is an information hub for Brooklyn College Computer Science students and faculty. Users can share original content, ask for assistance from other students, find collaborators, and have discussions across an array of curated communities.

### [Alpha Site](https://bc-app-class.herokuapp.com/)

## Setup
### Installation
- [Python3](https://www.python.org/downloads/) 
- Flask Web Framework (`pip3 install flask`)

### Requirements
- To install dependencies from the `requirements.txt` file: 
```pip3 install -r requirements.txt```
- When new Python libraries are required, update the `requirements.txt` file using the command and push the file to Github.
```pip3 freeze > requirements.txt```

## Deployment
### Running
***NOTE:** API connectivity is implemented. Please be careful when editting files as some files are necessary in order to keep the connection running.*

- Alpha release will be served on a server soon so that features can be continuously implemented.
- Navigate to the `/app` folder and execute `python3 app.py`

## Usage
### Notes 
- Make sure that the dependencies are up to date.
- Make sure that UnderDogs website is running in your web browser.

### Registration
*Alternatively, you can fast track to the [**Signing In**](#Login) section*

- Open the tab on the left side of the browser
- Select the `Register` button
- Enter your registration details into the fields.

### Login
First, make sure you have the API running and you note down the url ie `localhost:8080`

- Open the tab on the left and enter the following information into the fields:
- Username: `username`
- Password: `password`

## Contributing
Please keep check for recent pushes before pushing your work.
