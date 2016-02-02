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

mydict = {'F': {}, 'M': {}}

for line in b_file:

    name, sex, count = line.strip().split(',')
    last_letter = name[-1]

    if mydict[sex].get(last_letter):
        mydict[sex][last_letter] += int(count)
    else:
        mydict[sex][last_letter] = int(count)


b_file.close()

import string

print("Letter".ljust(8),'F'.rjust(8),'M'.rjust(8))
print("-"*26)

for letter in string.ascii_lowercase:
    print(letter.ljust(8), str(mydict['F'][letter]).rjust(8), str(mydict['M'][letter]).rjust(8))

#closed 
