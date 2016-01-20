
#Progam to crash with a connection error

import requests
url = "http://www.example.comma/"  #deliberate bad URL

printurl = "#  " + url
print(printurl)

resp = requests.get(url)
print (resp.status_code)
print (len(resp.text))
print (url)