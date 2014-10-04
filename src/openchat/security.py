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
		tmpStr = hashlib.sha1(tmpStr)
		if tmpStr == signature:
			return signature["echostr"]
		else:
			return None
	except Exception:
		return None

