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


mydict = {} 

for line in b_file:
    name, sex, count = line.strip().split(',')

    last_letter = name[-1]
    if mydict.get(last_letter):
    	mydict[last_letter] += int(count)
    else: 
    	mydict[last_letter] = int(count)

b_file.close()

import string

for letter in string.ascii_lowercase:
	print(letter+":", mydict[letter])

#closed 
