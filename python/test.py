
import requests

ENDPOINT = "http://127.0.0.1:5000"


resp = requests.post(ENDPOINT, data="hello")

if resp.status_code == 200:
    print(resp.content)
else:
    print(resp.status_code)