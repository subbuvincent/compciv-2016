from os.path import join
from glob import glob

tragedies_path = join('tempdata', 'tragedies', '*')
tragedies_files = glob(tragedies_path)

shakespeare_path = join('tempdata', '**', '*')
shakespeare_files = glob(shakespeare_path)

file_num = 0
total_lines = 0 
total_non_blank_lines = 0

for fname in shakespeare_files:
	
	file_num += 1
	
	txtfile = open(fname, 'r')

	#First get the line count, saved in line_num
	line_num = 0
	non_blank_lines = 0

	for line in txtfile:
		line_num += 1
		if line.strip() is not "":
			non_blank_lines += 1

	txtfile.close()

	print(fname, 'has', str(non_blank_lines), 'non-blank lines out of', str(line_num), 'total lines')

	total_lines += line_num
	total_non_blank_lines += non_blank_lines


print('All together, Shakespeare\'s', str(file_num), 'text files have:')
print(str(total_non_blank_lines), 'non-blank lines out of', str(total_lines), 'total lines')