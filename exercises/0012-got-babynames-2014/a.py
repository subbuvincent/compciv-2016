import os
import requests
from os.path import basename

#URLs 
babynames_url = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'

#file and dir setup
tempdir = 'tempdata'
baby_names_file = basename(babynames_url)

os.makedirs("tempdata", exist_ok = True)

#get file 
print('Downloading: ', babynames_url)
resp = requests.get(babynames_url)

# assuming the subdirectory tempdata has been created:
full_file_name = os.path.join(tempdir, baby_names_file)

b_file = open(full_file_name, 'w')

print('Writing file: ', full_file_name)
b_file.write(resp.text)
b_file.close()

# Count lines in Baby names file 
#b_file = open(full_file_name, 'r')

#line_num = 0
#for x in b_file:
#    line_num += 1
#   #print('Line', str(line_num), x.strip())

#b_file.close()

#
mytext = resp.text
line_count = len(mytext.splitlines())

print("There are", str(line_count), "lines in", full_file_name)

#closed 
