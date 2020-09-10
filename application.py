from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/getinvolved")
def getinvolved():
    return render_template("getinvolved.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")