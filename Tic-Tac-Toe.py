messages = {
    "dra": "Draw",
    "x": "X wins",
    "o": "O wins",
}

cells_split = ['   ', '   ', '   ']
cells = "".join(cells_split)
number_of_x = 0
number_of_o = 0


def print_board():
    print('---------')
    print('|', cells_split[0][0], cells_split[0][1], cells_split[0][2], '|')
    print('|', cells_split[1][0], cells_split[1][1], cells_split[1][2], '|')
    print('|', cells_split[2][0], cells_split[2][1], cells_split[2][2], '|')
    print('---------')


print_board()

list_of_coordinates = [[(1, 3), (2, 3), (3, 3)],
                       [(1, 2), (2, 2), (3, 2)],
                       [(1, 1), (2, 1), (3, 1)]]


def find_coordinates_index(coordinates):
    for index1, value1 in enumerate(list_of_coordinates):
        for index2, value2 in enumerate(value1):
            if value2 == coordinates:
                return index1, index2


def row_win(character, field):
    for row in field:
        row_count = 0
        for elem in row:
            if elem == character:
                row_count += 1
        if row_count == 3:
            return True


def column_win(character, field):
    if field[0][0] == field[1][0] == field[2][0] == character \
            or field[0][1] == field[1][1] == field[2][1] == character \
            or field[0][2] == field[1][2] == field[2][2] == character:
        return True


def cross_win(character, field):
    if field[0][0] == field[1][1] == field[2][2] == character\
            or field[0][2] == field[1][1] == field[2][0] == character:
        return True


def who_win(character, field):
    if row_win(character, field) or column_win(character, field) or cross_win(character, field):
        return True
    else:
        return False


while not who_win('X', cells_split) or not who_win('O', cells_split)\
        or (' ' not in cells and not who_win('X', cells_split) and not who_win('O', cells_split)):
    try:
        x, y = [int(i) for i in input('Enter the coordinates: ').split()]
        input_coordinates = (x, y)
    except ValueError:
        print("You should enter numbers!")
        continue
    if x > 3 or y > 3:
        print("Coordinates should be from 1 to 3!")
    elif 0 < x <= 3 and 0 < y <= 3:
        i, j = find_coordinates_index((x, y))
        if cells_split[i][j] != " ":
            print("This cell is occupied! Choose another one!")
        elif cells_split[i][j] == " ":
            if number_of_x == number_of_o:
                number_of_x += 1
                cells_split[i] = cells_split[i][:j] + 'X' + cells_split[i][j + 1:]
                cells = "".join(cells_split)
                print_board()
                if who_win('X', cells_split):
                    print(messages['x'])
                    break
                elif who_win('O', cells_split):
                    print(messages['o'])
                    break
                elif ' ' not in cells and not who_win('X', cells_split) and not who_win('O', cells_split):
                    print(messages['dra'])
                    break
            elif number_of_x > number_of_o:
                number_of_o += 1
                cells_split[i] = cells_split[i][:j] + 'O' + cells_split[i][j + 1:]
                cells = "".join(cells_split)
                print_board()
                if who_win('X', cells_split):
                    print(messages['x'])
                    break
                elif who_win('O', cells_split):
                    print(messages['o'])
                    break
                elif ' ' not in cells and not who_win('X', cells_split) and not who_win('O', cells_split):
                    print(messages['dra'])
                    break
