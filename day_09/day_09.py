def gen_new_value(values):
    if all(v == 0 for v in values[-1]):
        return values
    
    current_list = values[len(values)-1]
    new_data = []
    
    for i, value in enumerate(current_list):
        if i+1 < len(current_list):
            next_value = current_list[i+1]
            new_data.append(next_value - value)

    values.append(new_data)
    return gen_new_value(values)

def gen_history_values(values):
    last_value = 0
    values[-1].append(last_value)
    
    for i, v in enumerate(list(reversed(values))[1:]):
        last_value = v[0] - last_value
        if i == len(values[1:])-1: return(last_value)

with open('day_09/input.txt') as file:
    data = [list(map(int, line.replace('\n', '').split(' '))) for line in file.readlines()]
    # Part One
    total = 0
    for line in data:
        total += sum([values[-1] for values in gen_new_value([line])])
    print('[Part One]:', total)
    
    # Part Two
    total = 0
    for line in data:
        total += gen_history_values(gen_new_value([line]))
    print('[Part Two]:', total)