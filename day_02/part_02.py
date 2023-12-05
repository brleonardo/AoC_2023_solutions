import re

file = open('day_02/input.txt')
data = file.readlines()
file.close()
powers = []

def transform_game_data(index, game):
    s_data = game.replace(f'Game {index+1}:', '').replace(' ', '').replace('\n', '').replace(';', ',').split(',')
    return [re.findall(r'\d+|\w+', item) for item in s_data]

def find_min_amount(game):
    red = max([ int(g[0]) for g in game if g[1] == 'red'])
    green = max([ int(g[0]) for g in game if g[1] == 'green'])
    blue = max([ int(g[0]) for g in game if g[1] == 'blue'])
    return int(red) * int(green) * int(blue)

def sum_powers():
    g = [transform_game_data(i, game) for i, game in enumerate(data)]
    print('Sum of powers is:', sum([find_min_amount(game) for game in g]))

sum_powers()