from flask import Flask, render_template, request
import urllib.request
import webbrowser

app = Flask(__name__, template_folder=r'./templates') # Relative path to reach the templates folder

@app.route('/Regist_Pending/')
def pending():
    user = {'username': 'bla-bla-bla'}
    trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]
    return render_template('genLinks.html', name = "Bla", user = user, trendPorts = trendPorts)

@app.route('/Our_Team/')
def team():
    trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]
    return render_template('genLinks.html', name = "Bla", trendPorts = trendPorts)

@app.route('/Post_Submitted/')
def subm():
    user = {'username': 'bla-bla-bla'}
    trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]
    return render_template('postSubmitted.html', name = "Bla", user = user, trendPorts = trendPorts)

@app.route('/Write_Post/')
def create():
    user = {'username': 'bla-bla-bla'}
    trendPorts = [{'name': 'port1', 'mem': 18},{'name': 'port2', 'mem': 17},{'name': 'port3', 'mem': 16},{'name': 'port4', 'mem': 15},{'name': 'port5', 'mem': 14}]
    return render_template('writePost.html', name = "Bla", user = user, trendPorts = trendPorts)

if __name__ == "__main__":
    webbrowser.open_new("http://localhost:8080/Regist_Pending/")
    webbrowser.open_new("http://localhost:8080/Our_Team/")
    webbrowser.open_new("http://localhost:8080/Post_Submitted/")
    webbrowser.open_new("http://localhost:8080/Write_Post/")
    app.run('localhost', 8080, True, use_reloader=False)