import requests

url_cookie = "https://aes.cryptohack.org/flipping_cookie/get_cookie/"
url_check  = "https://aes.cryptohack.org/flipping_cookie/check_admin/"

def get_cookie():
    data = requests.get(url_cookie).text
    return eval(data)["cookie"]



# The script retrieves a cookie from a target URL. The `get_cookie` function sends a GET request to the endpoint and extracts the `cookie` field from the JSON response using `eval`. This prepares the cookie for subsequent operations.