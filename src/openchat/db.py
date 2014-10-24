import json
import pymongo

import openchat.config

db_connect = None

def connect():
	global db_connect
	global ready
	conf = openchat.config.setting.core.db
	try:
		conn = pymongo.Connection(conf.host.get(), conf.port.get())
	except KeyError:
		conn = pymongo.Connection("0.0.0.0", 27017)
		raise ValueError("openchat.config not load or missing keys")
	db_connect = conn
