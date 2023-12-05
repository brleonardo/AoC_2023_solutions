import re

file = open('day_02/input.txt')
data = file.readlines()
file.close()
final_data = []
colors = {'red': 12, 'green': 13, 'blue': 14}
red, green, blue = 12, 13, 14

def extract_game_data():
    for i, game in enumerate(data):
        sets = game.replace(f'Game {i+1}:', '').replace(' ', '').split(';')
        final_data.append([sort_set(pull) for pull in sets])

def sort_set(items):
    return dict(re.findall(r'\d+|\w+', pull) for pull in items.split(','))

def check_pull(pull):
    invalid = False

    for amount, color in pull.items():
        if int(amount) > colors[color]: return False
    return True

def sum_valid_ids():
    i_games = [i+1 for i, s in enumerate(final_data) for pull in s if not check_pull(pull)]
    v_games = [i+1 for i, d in enumerate(final_data) if i+1 not in i_games]
    print('The sum of valid ids is:', sum(v_games))
    
extract_game_data()
sum_valid_ids()