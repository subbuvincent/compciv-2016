
#Progam to count 'Applause' occurrences in SOTU 2016 Obama's

import requests
url = "https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/"

print("Getting Obama SOTU 2016 speech transcript...")
resp = requests.get(url)
print("Got it, counting \'Applause\' and \'<p>\'s now...")
print (resp.text.count('Applause'))
print (resp.text.lower().count('applause'))
print (resp.text.lower().count('<p>'))
print ("..done!")