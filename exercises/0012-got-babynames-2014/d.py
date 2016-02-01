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

print("\nTop baby girl names")

line = 1
while line <= 5:
    x = b_file.readline()
    name, sex, count = x.strip().split(',')
    print(str(line)+".",  name, str(count))
    line += 1


print("\nTop baby boy names")
line = 1
while line <= 5:
    x = b_file.readline()
    name, sex, count = x.strip().split(',')
    if 'M' in sex.upper():
    	print(str(line)+".",  name, str(count))
    	line += 1

b_file.close()

#closed 
