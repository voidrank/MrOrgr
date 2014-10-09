import xmltodict
import json

import openchat

def return_notification(args):
	args = xmltodict.parse(args)
	args = json.dumps(args)
	ToUserName = args["xml"]["ToUserName"]
	FromUserName = args["xml"]["FromUserName"]
	Content = args["xml"]["Content"]
	return 