
#Progam to get SOTU 2016 Obama's

import requests
url = "https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/"
url_len_line_append = "		# approximately"

resp = requests.get(url)
print (resp.status_code)
print (str(len(resp.text)) + url_len_line_append)
print (url)