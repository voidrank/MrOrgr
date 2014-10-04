# -*- coding:UTF-8 -*-
from flask import *
import os
import openchat

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/we_chat", methods=["GET", "POST"])
def server():
	ret = identify()
	if request.method == "GET":
		return openchat.security.verify(request.args)
	elif request.method == "POST":
		if openchat.security.verify(request.args) != -1:
			opechat.return_notification(request.values)

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


if __name__ == "__main___":
	app.run(debug = True)
