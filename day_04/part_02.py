import re

file = open('day_04/input.txt')
data = file.read()
file.close()
cards = []
total = []

def transform_data(data):
    t_cards = []
    for line in data.split('\n'):
        card_id = int(re.findall(r'\d+', line.split(':')[0])[0])
        c_numbers = line.split(':')[1].split('|')

        full_card = [card_id]
        [full_card.append(re.findall(r'\d+', numbers)) for numbers in c_numbers]
        t_cards.append(full_card)
    return t_cards

def find_total(s_cards, total):
    for card in s_cards:
        copies = []
        points = sum([1 for w in card[1] for c in card[2] if w == c])
        if points:
            copies = cards[card[0]:card[0]+points]
            total += copies
        if copies:
            find_total(copies, total)

print('Please wait...')
cards = transform_data(data)
find_total(cards, total)
print('Total of scratchcards:', len(cards) + len(total))