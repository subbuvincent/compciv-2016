import os
import requests
from os.path import basename

#URLs 
babynames_url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'

#file and dir setup
tempdir = 'tempdata'
baby_names_file = basename(babynames_url)


full_file_name = os.path.join(tempdir, baby_names_file)
b_file = open(full_file_name, 'r')

GOT_names_d = 0
GOT_names_k = 0

for x in b_file:

	name, sex, count = x.strip().split(',')
	if 'daenerys' in name.lower():
		GOT_names_d += int(count)
	elif 'khalees' in name.lower(): 
		GOT_names_k += int(count)
	elif 'khaless' in name.lower():
		GOT_names_k += int(count)

b_file.close()

print("Daenerys:", str(GOT_names_d))
print("Khaleesi:", str(GOT_names_k))

#closed 
