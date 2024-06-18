user_in = input("Enter cells: ")

row_one = user_in[:3]
row_two = user_in[3:6]
row_three = user_in[6:]

game_state = ''

x_win = ('XXX' in (row_one, row_two, row_three)) \
    or ('X' == row_one[0] and 'X' == row_two[0] and 'X' == row_three[0]) \
    or ('X' == row_one[1] and 'X' == row_two[1] and 'X' == row_three[1]) \
    or ('X' == row_one[2] and 'X' == row_two[2] and 'X' == row_three[2]) \
    or ('X' == row_one[0] and 'X' == row_two[1] and 'X' == row_three[2]) \
    or ('X' == row_one[2] and 'X' == row_two[1] and 'X' == row_three[0])
o_win = 'OOO' in (row_one, row_two, row_three) \
    or ('O' == row_one[0] and 'O' == row_two[0] and 'O' == row_three[0]) \
    or ('O' == row_one[1] and 'O' == row_two[1] and 'O' == row_three[1]) \
    or ('O' == row_one[2] and 'O' == row_two[2] and 'O' == row_three[2]) \
    or ('O' == row_one[0] and 'O' == row_two[1] and 'O' == row_three[2]) \
    or ('O' == row_one[2] and 'O' == row_two[1] and 'O' == row_three[0])
same_rows = row_one == row_two or row_two == row_three or row_one == row_three

x_chars = 0
o_chars = 0
empty_chars = 0
for char in user_in:
    if char == 'X':
        x_chars += 1
    elif char == 'O':
        o_chars += 1
    else:
        empty_chars += 1
x_o_diff = abs(x_chars - o_chars)

if x_win and not same_rows:
    game_state = 'X wins'
elif o_win and not same_rows:
    game_state = 'O wins'
elif x_win and o_win:
    game_state = 'Impossible'
elif x_o_diff > 1:
    game_state = 'Impossible'
elif (not x_win and not o_win) and empty_chars > 0:
    game_state = 'Game not finished'
elif (not x_win and not o_win) and empty_chars == 0:
    game_state = 'Draw'

row_one = '|' + row_one + '|'
row_two = '|' + row_two + '|'
row_three = '|' + row_three + '|'

row_one = ' '.join(row_one)
row_two = ' '.join(row_two)
row_three = ' '.join(row_three)

STROKE_LINE = '---------'

def draw_field():
    
    print(STROKE_LINE)
    print(row_one)
    print(row_two)
    print(row_three)
    print(STROKE_LINE)

    print(game_state)

draw_field()