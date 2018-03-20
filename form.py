#!/usr/bin/python2

import cgi
import commands
bgroup=cgi.FormContent()['bgroup'][0]
oname=cgi.FormContent()['oname'][0]
city=cgi.FormContent()['city'][0]
state=cgi.FormContent()['state'][0]
date=cgi.FormContent()['date'][0]
unit=cgi.FormContent()['unit'][0]
pincode=cgi.FormContent()['pincode'][0]
data="{0}_{1}_{2}_{3}_{4}_{5}_{6}".format(bgroup,oname,city,state,date,unit,pincode)
addData="""curl -X POST 127.0.0.1/mine -H 'Content-Type: application/json' -d '{ "data"={0} }' """.format(data)
status=commands.getstatusoutput(addData)
if status[0]==0:
	#Successful added to the blockchain
	print "Location: ./index.html"
	print ""
else:
	print "Error in adding Data "
	print status[1]

