# CISC 3140 - Summer 2019 Project [![Build Status](https://travis-ci.org/DataMascara/cisc3140-su19-project.svg?branch=master)](https://travis-ci.org/DataMascara/cisc3140-su19-project)
This is the repository for the group project in CISC 3140 Summer Session 2 2019 class at Brooklyn College.

## UnderDogs
UnderDogs is an information hub for Brooklyn College Computer Science students and faculty. Users can share original content, ask for assistance from other students, find collaborators, and have discussions across an array of curated communities.

## [Alpha Site](https://bc-app-class.herokuapp.com/)
## Launch Form/Feedback : https://forms.gle/DWKj28iPHTBTwDvK8
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
### Before Pushing
- Please run `git fetch` in order to update your current working branch with any recent commits pushed to the repo. This will help minimize the frequency at which your old code from another file overwrites the code that was recently updated in that file.

### Suggested (Ideal) Flow
The following method, known as Git Flow, is ideally the way we should be approaching updates to the repo:
- When you are working on a new feature or issue or anything, create a new branch with: ` git checkout -b <branch-name>`. Essentially, the branch name tends to be a short but descriptive name of the task being done in that branch. 
- When you are finished with your code, commit and push your branch to the repo using: ```git commit -am "<commit-message>"
git push origin <branch-name>```
- Lastly, create a pull request from your branch to the master branch, then the update is discussed and then merged through the pull request.

This method of updating the app, known as the Git Workflow, decreases the oppourtunity for old code to rewrite new code.
