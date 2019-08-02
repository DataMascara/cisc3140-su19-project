from flask import Flask, render_template, request
import urllib.request
import webbrowser

app = Flask(__name__, template_folder=r'./templates') # Relative path to reach the templates folder

# Testing File! Version 1.0 
# (Porbably will change when other templates are tested)
# Two routes, showing the two templates.
# Note the above argument to 'Flask' that has to do with the location of the templates folder: "template_folder=r'./templates'". 
# It must be here to make it find the templates.
# The pages 'http://localhost:8080/test1/' and 'http://localhost:8080/test/' open automatically in the browser for you to see the templates!
# This app runs on localhost port 8080.
# App automatically aliases flask, so that you don't need to type 'flask run' (happens due to the 'if __name__ == "__main__": app.run()' code below.)
# Just compile - and here you go!
# Enjoy!
# - Front End Team

@app.route('/')
@app.route('/test/')
def hello():
    return render_template('baseLoggedOut.html', title = "Logged Out :( ")

@app.route('/test1/')
def hello2():
    return render_template('baseLoggedIn.html', title = "Logged In :) ")

if __name__ == "__main__":
    webbrowser.open_new("http://localhost:8080/test1/")
    webbrowser.open_new("http://localhost:8080/test/")
    app.run('localhost', 8080, True, use_reloader=False)