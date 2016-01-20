import requests
url = "http://www.example.com/"
resp = requests.get(url)
print (resp.status_code)
print (len(resp.text))
print (url)