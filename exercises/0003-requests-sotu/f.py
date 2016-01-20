
#Progam to count 'Applause' and other occurrences in ALL SOTU Obama speeches 

import requests

#Get these URLs
url_set = ["https://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-address-joint-session-congress", 
"https://www.whitehouse.gov/the-press-office/remarks-president-state-union-address", 
"https://www.whitehouse.gov/the-press-office/2011/01/25/remarks-president-state-union-address",
"https://www.whitehouse.gov/the-press-office/2012/01/24/remarks-president-state-union-address",
"https://www.whitehouse.gov/the-press-office/2013/02/12/remarks-president-state-union-address",
"https://www.whitehouse.gov/the-press-office/2014/01/28/president-barack-obamas-state-union-address",
"https://www.whitehouse.gov/the-press-office/2015/01/20/remarks-president-state-union-address-january-20-2015",
"https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/"
]
url_len_line_append = "         # approximately"

print("Scraping Obama SOTU speech transcripts...")

year_start = 2009 

for x in range(8):
	year = year_start + x
	print(str(year), ':', url_set[x])
	resp = requests.get(url_set[x])
	print (str(len(resp.text)) + url_len_line_append)
	print (resp.text.lower().count('applause'))	
print("Finished!")
