from flask import Flask, render_template

app = Flask(__name__)

#Homepage
@app.route("/")
def hello_world():
	return render_template("hello.html")

#About me
@app.route("/about-me")
def about_me():
	return render_template("about-me.html")

#404
@app.errorhandler(404)
def page_not_found(error):
	return render_template("404.html"), 404