import hashlib

import openchat
import openchat.config

def verify(args):
	try:
		signature = args["signature"]
		timestamp = args["timestamp"]
		nonce = args["nonce"]

		token = openchat.config.core.verify.token.get()
		tmpArr = [token, timestamp, nonce]
		tmpArr.sort()
		tmpStr = "".join(tmpArr)
		tmpStr = hashlib.sha1(tmpStr).hexdigest()
		if tmpStr == signature:
			return str(args["echostr"])
		else:
			return str(None)
	except Exception:
		return "Error"

