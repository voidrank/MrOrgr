# -*- coding:UTF-8 -*-
from flask import *
import os
import bson.binary
import StringIO
from PIL import Image

import openchat

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

@app.route("/pic/<file_name>", methods=["GET"])
def pic_server(file_name):
	content, mime_type = openchat.image_server.return_pic(file_name)
	return Response(content, mimetype=mime_type)


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
