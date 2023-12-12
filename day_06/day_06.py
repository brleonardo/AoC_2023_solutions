import math

def calc_travel_distance(miliseconds, best_time):
    t_distance = (best_time - miliseconds) * miliseconds
    return t_distance

with open('day_06/input.txt') as file:
    times, distances = file.readlines()
    times = [int(t) for t in times.split(':')[1].split(' ') if t]
    distances = [int(d) for d in distances.split(':')[1].split(' ') if d]
    ways = []
    
    # Part 1
    for i, time in enumerate(times):
        count = 0
        for h_time in range(1, time):
            t_distance = calc_travel_distance(h_time, time)
            if t_distance > distances[i]:
                count += 1
        ways.append(count)
    
    print('Part 1 result:', math.prod(ways))
    
    # Part 2
    time = int(''.join(map(str, times)))
    distance = int(''.join(map(str, distances)))
    total = 0
    print('Please wait...')
    for t in range(1, time):
        t_distance = calc_travel_distance(t, time)
        if t_distance > distance:
            total += 1
    print('Part 2 result:', total)