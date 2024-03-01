from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/Home")
def Home():
    return render_template("Home.html",title="Home")

@app.route("/News")
def News():
    return render_template("News.html",title="News")

@app.route("/Adventure")
def Adventure():
    return render_template("Adventure.html",title="Adventure")

@app.route("/Sci-fi")
def Sci_fi():
    return render_template("Sci-fi.html",title="Sci-fi")

@app.route("/Comics")
def Comics():
    return render_template("Comics.html",title="Comics")

@app.route("/Historical")
def Historical():
    return render_template("Historical.html",title="Historical")

@app.route("/About_us")
def About_us():
    return render_template("About_us.html",title="About_us")

if __name__ == "__main__":
    app.run(debug=True)