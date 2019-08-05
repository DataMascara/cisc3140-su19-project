# Templates Folder README
### Version
1.1.0
### Log
08.05.2019 - Multi-Purpose General Links Template (+ corresponding CSS) added.
08.02.2019 - Two base templates were added.
### For the Back End Team (Base Templates):
 - All templates will 'extend' the base templates 'baseLoggedIn.html' and 'baseLoggedOut.html'.
 - For the current purpose of testing, use these templates to see if basic login features work.
 - When the real application will launch, these two templates shall not be rendered in any 'render_template' function call. The other templates shall be when they are uploaded. The reason is that the content in the base templates appears on every page, so they were just used for extension.
 - Every new version of a file (either the templates themselves or the CSS & JS) will be denoted by a new version number at the top, and probably the date of modification.
 - Following are descriptions of what arguments shall be passed to every template you render, which parts in the templates you should complete (fill-in), and what forms exist in each template:
 
### Arguments to Pass into 'render_template'

Because the base templates represent each and every webpage, each 'render_template' call should include the following arguments:
- When the user is logged in, a 'user' argument should be passed so that the particular template could choose to extend the 'baseLoggedIn' template
- When the user is signed out, **no** 'user' argument should be passed.
- Each and every 'render_template' call should pass the argument 'name' to be displayed as the title of the webpage in the browser.
- Each and every 'render_template' call should pass the argument 'ad', which is a decoded key-value dictionary (similar to what we did in assignment 1). Three keys should be contained: 'adurl', 'adtext' and 'imageurl'. These key names where chosen according to the names that the Database team gave to the keys in the tables they declared.
- Each and every 'render_template' call should pass the argument 'trendPorts', which is a 5-slot array of decoded dictionaries. Each dictionary has two keys: (1) 'name' (name of the port) (2) 'mem' (number of members). Either the Back End team or the Database team should choose 5 ports, whose details (name and number of members) will be displayed on the pages of **each and every user, whether logged in or logged out**. These shall not be randomized. Each and every user will be displayed with these particular 5 ports, and could choose if to subscribe to some or not. When the user is logged out, he or she **can only see** the names and # of members of the ports, but when they press 'subscribe', they are prompted to log in or register (so that the buttons do not work). When the user is logged in, the buttons will be included within a form whose information you could catch with 'request.form'. Here is an example of a valid content you could put inside the 'trendPorts' argument: 
[{ 'name':'CISCStuff', 'mem': 44}, { 'name':'foo', 'mem': 2}, { 'name':'BCClubs', 'mem': 1000}, { 'name':'datsStructs', 'mem': 19}, { 'name':'wow', 'mem': 16000}]
Note that you could choose **any** 5 ports, and that there is no need to order (sort) them according to highest number of members or alphabetically. Even port with small number of members will do (all of this I have been told by Joe from the Product group)
- When the user is logged out, and after he or she entered bad username or password, the argument 'errLogIn = True' should be passed so that an error message will be displayed on the screen.

### Stuff You Shall Fill-in the Base Templates
- Inside every of the two base templates are empty 'action' and 'href' attributes. Once you decide on the names of the routes to which various buttons / links will redirect the page, you should fill in this attributes. You are given the full freedom to choose your own route names! 
- Please note, that some of the forms across the base templates do not have an action attribute. These are **fake forms**. Do not add a new 'action' attribute to them. Just fill in where you see an empty 'action = "" ' attribute or empty 'href = "" ' attribute.
- Please upload your updates / changes to the repo after you make them so that the front end team could see the most relevant files. Thank you!

### Stuff for the Multi-Purpose General Links Template
- There is nothing additional to fill-into the Multi-Purpose General Links Template.
- Just decide (at a time) which argument to pass into the 'render-template' function:
  (1) If you pass 'about = True', the 'Our Team' page will be displayed to the user.
  (2) If you pass 'contact = True', the 'Contact Us' page will be displayed to the user.
  (3) If you pass 'terms = True', the 'Terms and Conditions' page will be displayed to the user.
  (4) If you pass none of these arguments, a 'nothing to display' message will be displayed to the user.
- The template was filled up with fake (and hopefully funny) info. You are welcome to take a look (and laugh if its really funny).
- The corresponding CSS file for this template was deposited in the 'static' folder.
- For any additional details, see the Jinja comments within the template itself.

### Forms in Every Template and the Info They Pass to You
- When the user is logged out, each template will have a sign in form. It has 3 input fields. The 1st two have the names 'username' and 'password', and the third is a sign in button with the unchanging value 'Sign in'.
- When the user is logged out, each template will have a registration-button form (we put this single button in a form so that it'll be easier to request the info from it.) It has 1 input field: a button with the name 'register' and unchanging value 'Register'. When the user clicks on it, it will redirect him or her to another page where there is a registration form (template still not uploaded).
- Each and every template will have a 'search bar'. It is located inside a form, and this input field has the name 'search'. Every time the user enters a string of text, this text will be search across **all existing** post names and contents, and a template with a list of posts that contain this text (still not uploaded) will be rendered.
- Each and every template will have a view port index form (we put this single button in a form so that it'll be easier to request the info from it.) It has 1 input field: a button with the name 'viewPortIndex' and unchanging value 'VIEW PORT INDEX'. When the user clicks on it, it will redirect him or her to another page where there is a list of all existing ports (template still not uploaded).
- When the user is logged in, every template has the trending ports form. It has 5 input fields, all of which are buttons. They differ only by their names: 'subscribe1', 'subscribe2', 'subscribe3', 'subscribe4', and 'subscribe5'. Do not modify or request their values, since their values are always changed! These buttons correspond to the 5 trending ports that everyone sees. When the user presses on a button, the id of the port will be added to the list of ports to which the user is subscribed. In other words, every user has a list of port ids to which he or she is subscribed, so if the user clicks, a new id will be added to the list. If the user clicks again, the id will be removed from there.
- When the user is logged in, every template has the user profile form. It has 1 input field, a button, with the unchanging value "User Profile". When the user clicks on it, it will redirect him or her to another page where the user could update his or her profile (template still not uploaded).
- When the user is logged in, every template has the dashboard form. It has 1 input field, a button, with the unchanging value "Dashboard". When the user clicks on it, it will redirect him or her to another page where the user could see the list of all his or her subscribed ports, submitted posts, submitted comments, and saved posts (template still not uploaded).
- When the user is logged in, every template has the user profile form. It has 1 input field, a button, with the unchanging value "Account Settings". When the user clicks on it, it will redirect him or her to another page where the user could update email / password / notifications (template still not uploaded).

New templates will be added during this weekend and the next week, with respective instructions about how to use them. If you have any questions about any of the above aspects, please do not hesitate to ask!
We are so thankful to you for you patience!
