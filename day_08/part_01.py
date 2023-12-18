def transform_data(data):
    s_part, e_part = data.split('=')[0].replace(' ', ''), data.split('=')[1].replace(' ', '')
    e_part = e_part.replace('(', '').replace(')', '').split(',')
    data = [s_part, e_part[0], e_part[1]]
    return data

with open('day_08/input.txt') as file:
    data = file.readlines()
    instructions = data[0].split('\n')[0]
    network = [transform_data(d.replace('\n', '')) for d in data[2:]]
    keys = [n[0] for i, n in enumerate(network)]
    current_location = 'AAA'
    steps = 0

    while current_location != 'ZZZ':
        steps += 1
        current_node = network[keys.index(current_location)]
        current_location = current_node[1] if instructions[0] == 'L' else current_node[2]
        instructions = instructions[1:] + instructions[0]

    print('[Part One]:', steps)