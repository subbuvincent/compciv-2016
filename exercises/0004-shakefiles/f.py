import os

fname = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')
txtfile = open(fname, 'r')

#First get the line count, saved in line_num
line_num = 0
for line in txtfile:
    line_num += 1
txtfile.close()

#print(str(line_num), 'lines')
#reopen and print only last N lines 

start_print_line_num = line_num - 5

#Reopen file and forward to start print point 
txtfile = open(fname, 'r')

for n in range(start_print_line_num): 
    txtfile.readline()

#bring pointer to 1-based correct line number 
n = n+1

for line in txtfile:
    n+=1
    the_line = str(n) + ": " + line.strip()
    print(the_line) 
    
txtfile.close()