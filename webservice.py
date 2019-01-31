from flask import Flask
import sys
import optparse
import time
from pycpu import getcpuinfo

# __aux = ""

app = Flask(__name__)

start = int(round(time.time()))

@app.route('/')
def mainfunct():
	global __aux
	return __aux

if __name__ == '__main__': 
	__aux = getcpuinfo()
	parser = optparse.OptionParser(usage='python3 webservice.py -p')
	parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
	(args, _) = parser.parse_args()
	if args.port == None:
		pt = 8080
	else:
		pt = int(args.port)
	app.run(host='0.0.0.0', port=pt, debug=False)
