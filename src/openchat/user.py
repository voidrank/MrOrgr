import datetime

import openchat

def login(user_id):
	try:
		user_id + ""
	except Exception:
		raise TypeError("user_id must be a string type")

	db = openchat.db.db_connect.openchat.user
	p = db.find_one(user_id)
	if p == None:
		return -1
	else:
		return p

def register(user_id):
	try:
		user_id + ""
	except Exception:
		raise TypeError("user_id must be a string type")

	db = openchat.db.db_connect.openchat.user
	p = db.insert({
		"user_id":{
			"register_time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			"last_login_time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			"nickname":user_id
		}}
		)
	if p == None:
		return -1
	else:
		return p

def user_event(user_id):
	p = login(user_id)
	if p == -1:
		return register(user_id)
	else:
		return p

if __name__ == "__main__":
	pass

