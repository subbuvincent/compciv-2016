import os
import requests
from os.path import basename

#URLs 
gmaps_url = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
mapzen_url = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'

#file and dir setup
tempdir = 'tempdata'
gmaps_jsonfile = 'googlemaps/stanford.json'
mapzen_jsonfile = 'mapzen/stanford.json'

os.makedirs('tempdata', exist_ok = True)
os.makedirs('tempdata/googlemaps', exist_ok = True)
os.makedirs('tempdata/mapzen', exist_ok = True)

#get file 
print('---')
print('Downloading from:', gmaps_url)
resp = requests.get(gmaps_url)

# assuming the subdirectory tempdata has been created:
gmaps_file_name = os.path.join(tempdir, gmaps_jsonfile)
g_file = open(gmaps_file_name, 'w')

print('Writing to:', gmaps_file_name)
g_file.write(resp.text)
g_file.close()
print("Wrote", len(resp.text.splitlines()), "and", len(resp.text), "characters")


print('---')
print('Downloading from:', mapzen_url)
resp = requests.get(mapzen_url)

mapzen_file_name = os.path.join(tempdir, mapzen_jsonfile)
m_file = open(mapzen_file_name, 'w')

print('Writing to:', mapzen_file_name)
m_file.write(resp.text)
m_file.close()
print("Wrote", len(resp.text.splitlines()), "and", len(resp.text), "characters")


#closed 
