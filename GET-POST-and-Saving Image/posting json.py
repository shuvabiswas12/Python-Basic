
# Posting json in python



import requests
import simplejson as json



url = "https://www.googleapis.com/urlshortener/v1/url"
headers = {"Content-Type": "application/json"}
payload = {"longurl": "http://exmaple.com"}

r = requests.post(url, json = payload, headers = headers) # posting json

print(json.loads(r.text), ["error"], ["code"])

print("\n========End Program=========\n")

print(r.headers) # returns headers




'''

NOTE:- for url shortner please go 'https://developers.google.com/url-shortener/v1/getting_started'


'''







