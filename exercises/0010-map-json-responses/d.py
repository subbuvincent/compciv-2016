import os
import requests
from os.path import basename
import json

#file and dir setup
tempdir = 'tempdata'
gmaps_jsonfile = 'googlemaps/stanford.json'

gmaps_file_name = os.path.join(tempdir, gmaps_jsonfile)
g_file = open(gmaps_file_name, 'r')

g_text = g_file.read()
g_file.close()

mydict = json.loads(g_text)

#get the results list 
results = mydict['results']

#cycle through results nested 
for x in results:
	for y in x['address_components']:
		print(y['long_name'], end="")
		if y['types'][0] != 'country':
			print(';', end=" ")
		else: 
			print("")

#closed 
