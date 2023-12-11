import re

file = open('day_04/input.txt')
total = 0

for n in file.read().split('\n'):
    n = n.split(':')[1].split('|')

    w_numbers, c_numbers = re.findall(r'\d+', n[0]), re.findall(r'\d+', n[1])

    points = 0
    for w in w_numbers:
        for c in c_numbers:
            if c == w:
                points = points*2 if points > 0 else 1
    total += points

print('Total points:', total)
file.close()