#!/usr/bin/python2

import cgi 
import commands
import os

bgroup=cgi.FormContent()['bg'][0]
city=[]

print "Content-type: text/html"
print 

d=commands.getoutput("curl -X GET 127.0.0.1:3001/blocks -H 'Content-Type: application/json' -s | jq '.[].data'").strip('[]').split('\n')
d.reverse()
d.pop

for value in d:
	templist=value.split('_')
	if templist[0].strip('"')==bgroup:
		if city.count(templist[6])==0:
			city.append(templist[5])
print city[0]



