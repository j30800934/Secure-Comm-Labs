import jwt 
import requests

x = jwt.encode({"username":"admin", "admin":True},"secret",algorithm="HS256")
url = "https://web.cryptohack.org/jwt-secrets/authorise/" + x +"/"
print(requests.get(url).text)

## crypto{jwt_secret_keys_must_be_protected}

# The code generates a JWT (JSON Web Token) with a payload containing {"username": "admin", "admin": True} and signs it using the HS256 algorithm and a secret key "secret". The JWT is then appended to a URL and sent as part of an HTTP request to the specified endpoint.

# The expected result is a response from the server indicating whether the authorization using the generated JWT was successful or not. The final output is the flag crypto{jwt_secret_keys_must_be_protected}, which hints that the secret key used to sign the JWT should be protected and not exposed. This is a security best practice to prevent unauthorized access or misuse.