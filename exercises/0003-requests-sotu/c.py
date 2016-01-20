
#Progam to crash with a missing schema error

import requests
url = "www.example.com"  #deliberately missed http:// in URL

printurl = "#  " + url
print(printurl)

resp = requests.get(url)
print (resp.status_code)
print (len(resp.text))
print (url)