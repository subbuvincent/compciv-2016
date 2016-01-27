
#b.py for assignment due on 26 Jan

import os
import requests
import shutil

tempdir = 'tempdata'
gzipfile = 'matty.shakespeare.tar.gz'

# assuming the subdirectory tempdata has been created:
full_file_name = os.path.join(tempdir, gzipfile)

print('Unpacking: ', gzipfile)
shutil.unpack_archive(full_file_name, extract_dir="tempdata")

#done