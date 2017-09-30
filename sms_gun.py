#!/usr/bin/python3
import sys
from twilio.rest import Client
#from twilio.rest import TwilioRestClient

accountSID='CENSURADO'
authToken='CENSURADO'


def go(goTwilio):
	try:
		message = goTwilio.messages.create(body=sys.argv[3], from_=sys.argv[2], to=sys.argv[1])
		print(str(message.to))
	except Exception as error:
		print("Error: ", error)

def main(ssid,authToken):
	goTwilio=Client(ssid,authToken)
	go(goTwilio)
	
		

if not len(sys.argv) < 2:
	main(accountSID,authToken)
else:
	print("Usage: ./%s <to> <from> <body>", sys.argv[0]) 
	exit(1)

