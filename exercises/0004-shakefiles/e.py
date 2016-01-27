
import os

file_name = os.path.join("tempdata", "tragedies", "hamlet")

hamlet_file = open(file_name, 'r')

line_num = 0
for x in hamlet_file:
    line_num += 1
#    print('Line', str(line_num), x.strip())
hamlet_file.close()

print(file_name, "has", line_num, "lines")