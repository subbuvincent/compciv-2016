
import os

file_name = os.path.join("tempdata", "tragedies", "hamlet")

h_file = open(file_name, 'r')
for x in range(1,6):
#    print('Line', str(x), h_file.readline().strip())
	print(h_file.readline().strip())
h_file.close()