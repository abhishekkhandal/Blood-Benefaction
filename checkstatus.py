#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

userhash=cgi.FormContent()['hash'][0]
getdonerhash="curl -X GET 127.0.0.1:3001/blocks -H 'Content-Type: application/json' -s | jq '.[].hash'"
d=commands.getoutput(getdonerhash)

getreceiverhash="curl -X GET 127.0.0.1:4001/blocks -H 'Content-Type: application/json' -s | jq '.[].data'"
r=commands.getoutput(getreceiverhash)

if userhash in r :
	print "Delivered"
elif userhash in d:
	print "Your Blood is still in freezer "
else:
	print "No Details Found! Please input the correct Hash ID again !"

print userhash

