import requests
import json

dd = {
  "device_id": "0777",
  "account": "string1",
  "device_name": "string777",
  "language": "string",
  "system_volume": 0,
  "media_volume": 0,
  "user_account": "string"
}

url = "http://127.0.0.1:8000/devicedata/"
url1 = "http://127.0.0.1:8000/devicedata/01"
url2 = "http://140.122.185.210/devicedata/"

html = requests.post(url2, json.dumps(dd))
#html = requests.delete(url)

#print(html.text)
