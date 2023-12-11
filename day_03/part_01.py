import re

file = open('day_03/input.txt')
data = file.read()
file.close()
ajd_numbers = []

p_number0 = r'\d+[^\d\.]\d+' # match two numbers with a valid symbol (not a period) in between
p_number1 = r'.\d+.' # any number with symbols after or before
p_number2 = r'\d+' # any number
p_symbol = r'[^\.|\d]' # anything that is not a period or a number

def transform_string(string):
    return ''.join(['.' if s.isdigit() else s for s in string])

#  match 1 -> two numbers with a valid symbol in between
def first_match(data):
    for number in re.findall(p_number0, data):
        [ajd_numbers.append(int(n)) for n in number.split('*')]
        data = data.replace(number, transform_string(number))
    return data

# match 2 -> numbers with a symbol before or after
def second_match(data):
    for number in re.findall(p_number1, data):
        start, end = number[0], number[-1]
        if not start.isdigit() and start != '.' or not end.isdigit() and end != '.':
            my_number = ''.join([s for s in number if s.isdigit()])
            ajd_numbers.append(int(my_number))
            data = data.replace(number, transform_string(number))
    return data

def calc_adj(data1, data2):
    if not data2: return False
    x1, x2 = data1['span']
    data_y = [data_y['span'] for data_y in data2]
    return [True for y1, y2 in data_y if y1 >= x1-1 and y1 <= x2]
    return False

def extract_f_data(matches):
    return [{'span': i.span(), 'match': i.group()} for i in matches]

def match_line(line, mid):
    return re.finditer(p_number2, line) if mid else re.finditer(p_symbol, line)

def sum_part_numbers(lines):
    for index, line in enumerate(lines):
        m1, m2, m3 = [], [], []
        f_data = []
        # extract the data from each match and append it as a dict
        f_data.append(extract_f_data(match_line(lines[index-1], False)) if index > 0 else [])
        f_data.append(extract_f_data(match_line(line, True)))
        f_data.append(extract_f_data(match_line(lines[index+1], False)) if index != len(lines)-1 else [])
        # check adjacents
        [ajd_numbers.append(int(data['match'])) for data in f_data[1] if calc_adj(data, f_data[0]) or calc_adj(data, f_data[2])]
    
    print('The sum of all gear ratios:', sum(ajd_numbers))

data = first_match(data)  # transforming data
data = second_match(data) # transforming data
sum_part_numbers(data.split('\n'))