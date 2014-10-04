import hashlib

import openchat

def verify(args):
	signature = args["signature"]
	timestamp = args["timestamp"]
	nonce = args["nonce"]

	token = openchat.config.setting.core.verify.token.get()
	tmpArr = [token, timestamp, nonce]
	tmpArr.sort()
	tmpArr = tuple(tmpArr)
	tmpStr = "%s%s%s" % tmpArr
	tmpStr = hashlib.sha1(tmpStr).hexdigest()
	if tmpStr == signature:
		return str(args["echostr"])
	else:
		return "bad man!!!"

