from flask import Flask, render_template

app = Flask(__name__)

#Homepage
@app.route("/")
def hello_world():
	return render_template("index.html", title="Homepage")
#Music
@app.route("/music")
def music():
	return render_template("music.html")
#About me
@app.route("/about-me")
def about_me():
	return render_template("about-me.html")
#Press kit
@app.route("/press-kit")
def press_kit():
	return render_template("press-kit.html")
#Tour
@app.route("/tour")
def tour():
	return render_template("tour.html")
@app.route
#404
@app.errorhandler(404)
def page_not_found(error):
	return render_template("404.html"), 404
