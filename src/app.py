# -*- coding:UTF-8 -*-
from flask import *
import os
import openchat
import bson.binary

app = Flask(__name__)
app.secret_key = os.urandom(24)
openchat.config.load("config.json")
openchat.db.connect()

@app.route("/we_chat", methods=["GET", "POST"])
def server():
	if request.method == "GET":
		return openchat.security.verify(request.args)
	elif request.method == "POST":
		if openchat.security.verify(request.args) == 1:
			return str(opechat.return_notification(request.values))
		
@app.route("/upload", methods=["GET", "POST"])
def upload():
	if request.method == "POST":
		f = request.files["uploaded_file"]
		print f.read()
		return redirect("/upload")
	elif request.method == "GET":
		return render_template("upload_pic.html")	

@app.route("/pic", methods=["GET","POST"])
def pic_server():
	pass


'''
@app.route("/")
def index():
	return render_template("index.html", msg = session)

@app.route("/admin")
def admin():
	if "admin" in session:
		return render_template("admin.html", msg = session)
	else:
		abort("403")

@app.route("/login")
def login():
	if "admin" in session:
		return redirect(url_for("admin"))
	else:
		return render_template("login.html")
'''


if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0", port = 80)
