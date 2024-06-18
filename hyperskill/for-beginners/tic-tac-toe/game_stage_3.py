field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def take_game_state():

    field_string = [char for inner in field for char in inner]
    field_string = ''.join(field_string)
    row_one = field_string[:3]
    row_two = field_string[3:6]
    row_three = field_string[6:]

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
    for char in field_string:
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

    return game_state


def field_change_state(move, symbol):
    global field
    field[move[0]][move[1]] = symbol
    field_draw(field)


def field_draw(field_state):
    row_1, row_2, row_3 = field_state
    row_1 = '| ' + ' '.join(row_1) + ' |'
    row_2 = '| ' + ' '.join(row_2) + ' |'
    row_3 = '| ' + ' '.join(row_3) + ' |'
    print('---------')
    print(row_1)
    print(row_2)
    print(row_3)
    print('---------')


field_draw(field)


# Take user move coordinates and validate values
user_move = []
def take_and_validate_move():
    # X and O symbol trigger: True(X), False(O)
    symbol_trigger = True
    symb = ''
    while True:
        global user_move
        user_move = input("Enter the coordinates: ").split()
        if user_move[0].isdigit() and user_move[1].isdigit():
            # Translate coordinates from grid index to list index
            user_move = [int(num) - 1 for num in user_move]
            if (0 > user_move[0] or user_move[0] > 2) or (0 > user_move[1] or user_move[1] > 2):
                print("Coordinates should be from 1 to 3!")
            elif field[user_move[0]][user_move[1]] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                if symbol_trigger == True:
                    symb = 'X'
                    symbol_trigger = not symbol_trigger
                else:
                    symb = 'O'
                    symbol_trigger = not symbol_trigger
                field_change_state(user_move, symb)
                game_state = take_game_state()
                if game_state == 'X wins' or game_state == 'O wins' or game_state == 'Draw':
                    print(game_state)
                    break
        else:
            print("You should enter numbers!")

take_and_validate_move()