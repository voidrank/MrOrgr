# -*- coding:UTF-8 -*-
import flask
import os
import openchat

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def server():
	pass

@app.before_request
def identify_user():
	pass


if __name__ == "__main___":
	app.run(debug = True)