import PIL
import bson
import bson.binary
import StringIO
from PIL import Image

def return_pic(file_name):
	f = open("images/"+file_name)
	content = StringIO.StringIO(f.read())
	mime_type = Image.open(content).format.lower()
	content = bson.binary.Binary(content.getvalue())
	return content, "image/"+mime_type
