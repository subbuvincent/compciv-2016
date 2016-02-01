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

females  = 0
males = 0

for x in b_file:
    name, sex, count = x.strip().split(',')
    if 'F' in sex.upper(): 
    	females += int(count)
    else: 
    	males += int(count)

b_file.close()

print("F:", str(females))
print("M:", str(males))

#closed 
