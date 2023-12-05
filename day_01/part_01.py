import re

file = open('day_01/input.txt')
data = file.readlines()
file.close()

c_values = [re.findall(r'\d', line) for line in data]
total = sum([int(c[0]+c[-1]) for c in c_values])
print(f'Sum of calibration values:', total)