import re

file = open('day_03/input.txt')
data = file.read()
file.close()
lines = data.split('\n')
gear_ratios = []

p_symbol0 = r'\*' # any 'star'
p_symbol1 = r'\d+\*\d+' # match any 'star' and numbers before or after
p_symbol2 = r'\d+\.\d+' # match any number with period in between
p_symbol3 = r'\d+\*|\*\d+' # match any 'star' and numbers before or after

def calc_topbot_ratios(index, s_span):
    ratios = re.finditer(p_symbol2, lines[index]) or []
    for ratio in ratios:
        r1, r2 = ratio.group().split('.')[0], ratio.group().split('.')[1]
        p_period = r'(?<=' + r1 + ')\.(?='+ r2 +')'
        period_match = re.finditer(p_period, lines[index])
        for pm in period_match:
            if s_span == pm.span():
                # replace original
                # save ratios
                new_string = '.'*len(r1)+ '.' +'.'*len(r2)
                lines[index] = lines[index].replace(ratio.group(), new_string)
                gear_ratios.append(int(r1)*int(r2))

def check_top_bot(index, match):
    numbers = re.finditer(r'\d+', lines[index])
    is_before = True if match.group().split('*')[1] else False
    match_index = index+1 if is_before else index-1
    symbol_number = match.group().split('*')[0] or match.group().split('*')[1]
    y1, y2 = match.span()
    
    for number in numbers:
        x1, x2 = number.span()
        if (is_before and x2 <= y2 and x2 >= y1) or (not is_before and x1 <= y2 and x1 >= y1):
            # replace match that has a '*' before or after
            lines[match_index] = lines[match_index].replace(match.group(), '.'*len(match.group()))
            # replace adjacent number
            lines[index] = lines[index].replace(number.group(), '.'*len(number.group()))
            gear_ratios.append(int(number.group()) * int(symbol_number))

def check_mid(index, start, end):
    if index-1 < 0 or index+1 >= len(lines): return
    
    top_line, bot_line = re.finditer(r'\d+', lines[index-1]), re.finditer(r'\d+', lines[index+1])
    value1 = [tl.group() for tl in top_line if end >= tl.span()[0] and start <= tl.span()[1]]
    value2 = [bl.group() for bl in bot_line if end >= bl.span()[0] and start <= bl.span()[1]]

    if value1 and value2:
        gear_ratios.append(int(value1[0]) * int(value2[0]))

# check if the line has in between stars
def match_star_between(index):
    ratios = re.findall(p_symbol1, lines[index]) or []
    for r in ratios:
        lines[index] = lines[index].replace(r, '.'*len(r)) # replace match with periods
        gear_ratios.append(int(r.split('*')[0]) * int(r.split('*')[1]))

# check if a number with period in between has a 'star' symbol
# at the same position as the period in top line or bot line
def match_period_between(index):
    index_top, index_bot = index-1, index+1
    for s in re.finditer(p_symbol0, lines[index]):
        if index_top >= 0: calc_topbot_ratios(index_top, s.span())
        if index_bot < len(lines): calc_topbot_ratios(index_bot, s.span())

def match_before_after(index):
    index_top, index_bot = index-1, index+1
    for number in re.finditer(p_symbol3, lines[index]):
        if index_top >= 0: check_top_bot(index_top, number)
        if index_bot < len(lines): check_top_bot(index_bot, number)
  
def match_mid_line(index):
    symbols = re.finditer(p_symbol0, lines[index])
    for symbol in symbols: check_mid(index, symbol.span()[0], symbol.span()[1])

for index, line in enumerate(lines):
    match_star_between(index)
    match_period_between(index)
    match_before_after(index)
    match_mid_line(index)

print('The sum of gear ratios is:', sum(gear_ratios))