
#b.py for assignment due on 26 Jan

import os
import requests

#URLs 
gzipurl = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'

#file and dir setup
tempdir = 'tempdata'
gzipfile = 'matty.shakespeare.tar.gz'

#get zip 
print('Downloading: ', gzipurl)
resp = requests.get(gzipurl)

# assuming the subdirectory tempdata has been created:
full_file_name = os.path.join(tempdir, gzipfile)

zfile = open(full_file_name, 'wb')

print('Writing file: ', full_file_name)
zfile.write(resp.content)

zfile.close()
#closed 
