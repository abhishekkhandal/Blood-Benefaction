#!/usr/bin/python2

import cgi
import commands
import cgitb

import qrcode
from PIL import Image
cgitb.enable()

def head():
	print "content-type: text/html"
	print


userhash=cgi.FormContent()['hash'][0]

getdonerhash="curl -X GET 127.0.0.1:3001/blocks -H 'Content-Type: application/json' -s | jq '.[].hash'"
d=commands.getoutput(getdonerhash)

getreceiverhash="curl -X GET 127.0.0.1:4001/blocks -H 'Content-Type: application/json' -s | jq '.[].data'"
r=commands.getoutput(getreceiverhash)

def qrcode(self, ticketnumber = 'hash'):
	img = qrcode.make(ticketnumber)
	cp.response.headers['Content-Type'] = "image/png"
	buffer = StringIO.StringIO()
	img.save(buffer, 'PNG')
	return buffer.getvalue()

img = qrcode('http://localhost/Blood-Benefaction/checkstatus.py?hash={0}').format(hash)
print img
if userhash in r :
	head()
	print "Delivered"
elif userhash in d:
	head()
	print "Your Blood is still in freezer "
	#print "<img src=\"{0}\">".format(img)
else:
	head()
	print "No Details Found! Please input the correct Hash ID again !"

print userhash

