# Duplicate machine - The purpose of this script is to copy the data from a file to an empty file

import math

FILENAME1 = r'Exercise.txt'
FILENAME2 = r'Solution.txt'

sol_file = open(FILENAME2, 'a')

with open(FILENAME1, 'r') as ex_file:
    for line in ex_file:
        line = line.split(" ")
        line.append('=')
        
        if line[1] == '+':
            line.append(line[0]+line[1])
        line = ' '.join(line)
        sol_file.write(line)
sol_file.close()
