#!/usr/bin/env python

import urllib
import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)
	print("Request:")
	print(json.dumps(req, indent=4))
	res = makeWebhookResult(req)
	res = json.dumps(res, indent=4)
	print(res)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r

def makeWebhookResult(req):
	result = req.get("result")
	parameters = result.get("parameters")
	queryText = parameters.get("any")
	
	if req.get("result").get("action") == "get-code":
		speech=callHackerRankApi(queryText)
		print(speech)
	
		return {
		"speech": speech,
		"displayText": speech,
		"data":{"slack":{"text":speech}}, 
		#"contextOut": [],
		"source": "webhook"
		}
	if req.get("result").get("action") == "get-query":
		speech = queryText + "We are yet to integrate query response. Please wait for our next update"
		print(speech)
		return {
		"speech": speech,
		"displayText": speech,
		"data":{"slack":{"text":speech}},
		#"contextOut": [],
		"source": "webhook"
		}
def callHackerRankApi(code):


	'''
	Go here and generate your API key.
	https://www.hackerrank.com/api/docs/
	'''
	
	data = [
		('source', code),
		('lang', '30'),
		('testcases', '["1"]'),
		('api_key', 'your_api_key'), 
	]
	response = requests.post('http://api.hackerrank.com/checker/submission.json', data=data)
	print(response)
	sid=response.json()['result']['stdout']
	if sid is None:
		error = response.json()['result']['compilemessage'].split('\n')
		print(error[3])
		return (error[3].rstrip()) #removing newline at end. yet to push
	return(sid[0])

if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))

	print ("Starting app on port %d" % port)

	app.run(debug=True, port=port, host='0.0.0.0')

