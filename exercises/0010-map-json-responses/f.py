import os
import requests
from os.path import basename
import json

#file and dir setup
tempdir = 'tempdata'
mapz_jsonfile = 'mapzen/stanford.json'

mapz_file_name = os.path.join(tempdir, mapz_jsonfile)
m_file = open(mapz_file_name, 'r')

m_text = m_file.read()
m_file.close()

mz_dict = json.loads(m_text)

print("type:", mz_dict['type'])
print("text:", mz_dict['geocoding']['query']['text'])
print("size:", mz_dict['geocoding']['query']['size'])
print("boundary.country:", mz_dict['geocoding']['query']['boundary.country'])

#cycle through results nested 
#for x in results:
#	print(x['formatted_address'] + ';', end="")
#	print(str(x['geometry']['location']['lng']) + ';', end="")
#	print(str(x['geometry']['location']['lat']), end="")
#	print("")

#closed 
