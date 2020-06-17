import urllib.request
import json

url = 'https://api.covid19api.com/summary'

with urllib.request.urlopen(url) as response:
    data = response.read()
    y = json.loads(data)
    print(y)
