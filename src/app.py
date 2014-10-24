# -*- coding:UTF-8 -*-
from flask import *
import os
import bson.binary
import StringIO
import xmltodict
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
			print str(xmltodict.parse(request.values))

@app.route("/pic/<file_name>", methods=["GET"])
def pic_server(file_name):
	content, mime_type = openchat.image_server.return_pic(file_name)
	return Response(content, mimetype=mime_type)

@app.route("/barrage_live", methods=["GET"])
def barrage_live():
	return render_template("barrage_live_2.html")

@app.route("/ajax/barrage_live")
def ajax_barrage_live():
	p = ["hahaha","hehehe"]
	return str(p)

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
