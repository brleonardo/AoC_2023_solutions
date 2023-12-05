import re

file = open('day_01/input.txt')
data = file.read()
file.close()
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_replace = ['one1one', 'two2two', 'three3three', 'four4four', 'five5five', 'six6six', 'seven7seven', 'eight8eight', 'nine9nine']

def find_calibration_values():
    t = transform_data(data)
    c_values = [re.findall(r'\d', line) for line in t.splitlines()]
    print('The sum of the true calibration values is:', sum(int(c[0] + c[-1]) for c in c_values))

def transform_data(data):
    for i, n in enumerate(numbers):
        data = data.replace(n, num_replace[i])
    return data

find_calibration_values()