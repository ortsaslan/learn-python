field_start_in = input("Enter cells: ").replace("_", " ")

field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def is_user_win(symbol):
    pass

def field_initialize(field_init):
    global field
    field[0][0] = field_init[0]
    field[0][1] = field_init[1]
    field[0][2] = field_init[2]
    field[1][0] = field_init[3]
    field[1][1] = field_init[4]
    field[1][2] = field_init[5]
    field[2][0] = field_init[6]
    field[2][1] = field_init[7]
    field[2][2] = field_init[8]

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

field_initialize(field_start_in)
field_draw(field)

# Take user move coordinates and validate values
user_move = []
def validate_move():
    while True:
        global user_move
        user_move = input("Enter the coordinates: ").split()
        if user_move[0].isdigit() and user_move[1].isdigit():
            user_move = [int(num) - 1 for num in user_move]
            if (0 > user_move[0] or user_move[0] > 2) or (0 > user_move[1] or user_move[1] > 2):
                print("Coordinates should be from 1 to 3!")
            elif field[user_move[0]][user_move[1]] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                break
        else:
            print("You should enter numbers!")

validate_move()

def field_change_state(move, symbol = "X"):
    global field
    field[move[0]][move[1]] = symbol
    field_draw(field)
    #is_user_win()

field_change_state(user_move)

