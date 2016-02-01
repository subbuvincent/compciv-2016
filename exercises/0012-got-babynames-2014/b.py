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

names = 0
for x in b_file:
	x_items = x.split(',')
	names += int(x_items[2])

b_file.close()

print("There are", str(names), "babies whose names were recorded in 2014")

#closed 
