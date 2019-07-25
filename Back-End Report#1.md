# **Back-end Weekly Checkpoint #1**


**(Q1)** Discuss in teams specifically would like to accomplish over the next few weeks from the list of features the class brainstorming session the day before

### Over the coming weeks we'd like to accomplish:

- Connect to a python module that directly interfaces with a SQL database
- Make a barebones API that has CRUD functionality for the front end to hit
    - Understand how we can use JSON responses to signal success/failure of operation

**(Q2)** How is your team breaking down work, how are planning to tackle things in weekly increments, in what order, when do you expect to finish each feature?* 

- We are using [notion.so](http://notion.so) and it's roadmap template to make and assign "cards" that have due dates and assigned developers.
- We expect to have a functional CRUD(Create, Read, Update, Delete) API by 7/28.
- The order of tasks are roughly drafted as:
    1. Get barebones API connected to  DB's python module by 7/30
        1. Send barebones API to QA for testing, keep in contact.
    2. Be able to take a login request from the front end, send it to the db and respond to the front end, having them "log in" a user by 8/1

**(Q3)***:Would your team prefer other teams to contact a representative of your team or all team members?*  

- Currently Mark has been the main point of contact to both the Front-end and database team, however all members can be reached if necessary. Feel free to contact mark at MarkGoldstein12@gmail.com or on the slack @Mark Goldstein, if that's your thing.

**(Q4)** Your team will give a short presentation to the class, a brief summary, so all the teams have an idea of what your team will aim for.* 

### We are planning to make the back-end  FLASK for our API.

- The api will be called from the front end's javascript, preferably sending the API/us JSON with identifiable information.
- **For example**, say a user wants to delete a post, we'd have a API end point set up that takes a DELETE request. IE 1.127.0.0.0/user/delete-post.
    - We'd parse the front end's JSON for the user identifier and post id to delete.
    - Call the databases module method that takes those two fields and deletes a post.
    - The database will process the delete based off of of our relayed request, and then return a response if the post was deleted or not.
    - Finally we will return a response to the front end via JSON signaling the databases response.

### Current assumptions

- The front end will handle all VIEWS (what the user sees), so our flask API will not return a jinja2 template based off the user input. This would be done in HTML and Javascript. Rather we will send the front end's javascript responses that they will process and use to make the HTML page interactive. If we were using jinja2 from the backend to render pages we would be limiting the front end's role of being able to use javascript's convenient ways to edit the page and grab elements ie  `element = document.querySelector("thing to select");`
    - Please be in contact with us if you have other plans on how to render views.
- Database team will make a  python module that connects to a MYSQL hosted database.
    - The python module will include methods for full CRUD functionality including specific cases based off of the Product team's decided user actions.
        - This way the backend flask API can call the methods of the database module based on what JSON we get from the front end requests.
    - The database python module will respond in JSON or python dictionaries.
        - Methods will be commented on what is expected as input (ie params and what they are, like python objects, json etc.) and what the responses can be expected to look like (ie JSON, python dictionary ect.)

From a high level we imagine the database, back-end and front end relation ship to flow like this:

![](https://i.imgur.com/CFD2POY.png)

## Our ask for other teams:

- Contact us if there is a feature that you could use our support with.
- **Database team:** Get Documentation/Specifications on how they expect us to send data (ie a username to lookup) and how they will send it back (ie as a JSON).
    - Detailed comments from method headers would be
- **Front-end team :** Get Documentation/specs (seems like they wrote up a lot of this already and posed it. TY! We will review it and respond) on how they expect us to send data (ie a username to lookup) and how they will send it back (ie as a JSON).
- Any feedback and suggestions on how we should set up the app's API/Backend architecture.
- Review our code and readme on our branch named [here](https://github.com/DataMascara/cisc3140-su19-project/tree/backend-experimental-bare-bones) or, if you're not logged in, read our current readme here [https://rentry.co/xbifn](https://rentry.co/xbifn)

As a team we are excited by this opportunity to work together with the class' teams. We look forward to learning together how quick, "start-up" style software development with teams work. Please feel free to open more channels of communication at anytime!  
