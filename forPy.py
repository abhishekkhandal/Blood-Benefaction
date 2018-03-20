#!/usr/bin/python

import commands

BG_RAW_DATA = commands.getoutput("curl -X GET 127.0.0.1:3001/blocks -H 'Content-Type: application/json' -s | jq '.[].data'").strip('[]').strip('\n').split('\n')
index = 0
for i in range(len(BG_RAW_DATA)):
	bg = commands.getoutput("curl -X GET 127.0.0.1:3001/blocks -H 'Content-Type: application/json' -s | jq'.[].data'").strip('[]').strip('\n').split('\n')[index].split('_')
	index += i
	if bg == 'A+':
		print bg
	else:
		print bg