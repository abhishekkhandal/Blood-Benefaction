#!/usr/bin/python2

import cgi
import commands

donorNumber=cgi.FormContent()['donor-number'][0]
bloodType=cgi.FormContent()['blood-type'][0]
RhFactor=cgi.FormContent()['rh-factor'][0]
unit=cgi.FormContent()['unit-amount'][0]
dateDonated=cgi.FormContent()['dateDonated'][0]

orgName=cgi.FormContent()['org-name'][0]
orgNumber=cgi.FormContent()['org-number'][0]
orgState=cgi.FormContent()['org-state'][0]
orgCity=cgi.FormContent()['org-city'][0]
pincode=cgi.FormContent()['pincode'][0]

curl = "curl -X POST 127.0.0.1:3001/mine -H 'Content-Type: application/json' -d '{\"data\":"
data="""\"{0},{1}_{2},{3},{4},{5},{6},{7},{8},{9}\"""".format(donorNumber,bloodType,RhFactor,unit,dateDonated,orgName,orgNumber,orgCity,orgState,pincode)
addData = curl + data + "}'"

status=commands.getstatusoutput(addData)
if status[0]==0:
	#Successful added to the blockchain
	print "Location: ./blood-status.py"
	print ""
else:
	print "Error in adding Data "
	print status[1]

