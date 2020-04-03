import requests
from pprint import pprint

key = "fd0d5ef5e7044359828debed2f6a5aa7"
params = {
    "location": "auto_ip",
    "key": key
}
url = "https://free-api.heweather.net/s6/weather?location=qingdao&key={}".format(key)

r = requests.post(url)
print(r.url)
d = r.json()
print(d)
