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

feature_list = mz_dict['features']

for f in feature_list:
		print(f['properties']['label'] + ";", end="")
		print(str(f['properties']['confidence']) + ";", end="")
		print(str(f['geometry']['coordinates'][0]) + ';', end="")
		print(str(f['geometry']['coordinates'][1]))

#closed 
