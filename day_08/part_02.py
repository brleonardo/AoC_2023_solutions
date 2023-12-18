from threading import Thread
import math

steps = []

def transform_data(data):
    s_part, e_part = data.split('=')[0].replace(' ', ''), data.split('=')[1].replace(' ', '')
    e_part = e_part.replace('(', '').replace(')', '').split(',')
    data = [s_part, e_part[0], e_part[1]]
    return data

def count_steps(index, start_nodes, network, instructions):
    global steps
    count = 0
    while not start_nodes[index].endswith('Z'):
        node = [node for node in network if node[0] == start_nodes[index]][0]
        start_nodes[index] = node[1] if instructions[0] == 'L' else node[2]
        instructions = instructions[1:] + list(instructions[0])
        count+=1
    steps.append(count)

with open('day_08/input.txt') as file:
    data = file.readlines()
    instructions = [char for char in data[0] if char != '\n']
    network = [transform_data(n.replace('\n', '')) for n in data[2:]]
    start_nodes = [n[0] for n in network if n[0].endswith('A')]

    for index in range(len(start_nodes)):
        Thread(target=count_steps, args=[index, start_nodes, network, instructions]).start()

    print('Please wait...')
    while True:
        if len(steps) == len(start_nodes):
            print('[Part Two]:', math.lcm(*steps))
            break