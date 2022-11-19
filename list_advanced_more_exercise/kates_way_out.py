def valid_position(row, col, matrix):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return True
    return False


def next_position(row, col, matrix):
    if matrix[row][col] == ' ':
        return True
    return False


def is_last_move(row, col, matrix, size):
    if row == 0 or row == size - 1 or col == 0 or col == len(matrix[row]) - 1:
        return True
    return False


def find_next_position(row, col, matrix):
    # row - 1, col - 1
    # if valid_position(row - 1, col - 1, matrix):
    #     if next_position(row - 1, col - 1, matrix):
    #         matrix[row - 1][col - 1] = 'k'
    #         row = row - 1
    #         col = col - 1
    #         return row, col, True
    # row - 1, col
    if valid_position(row - 1, col, matrix):
        if next_position(row - 1, col, matrix):
            matrix[row - 1][col] = 'k'
            row = row - 1
            col = col
            return row, col, True
    # row - 1, col + 1
    # if valid_position(row - 1, col + 1, matrix):
    #     if next_position(row - 1, col + 1, matrix):
    #         matrix[row - 1][col + 1] = 'k'
    #         row = row - 1
    #         col = col + 1
    #         return row, col, True

    # row, col - 1
    if valid_position(row, col - 1, matrix):
        if next_position(row, col - 1, matrix):
            matrix[row][col - 1] = 'k'
            row = row
            col = col - 1
            return row, col, True
    # row, col + 1
    if valid_position(row, col + 1, matrix):
        if next_position(row, col + 1, matrix):
            matrix[row][col + 1] = 'k'
            row = row
            col = col + 1
            return row, col, True

    # row + 1, col - 1
    # if valid_position(row + 1, col - 1, matrix):
    #     if next_position(row + 1, col - 1, matrix):
    #         matrix[row + 1][col - 1] = 'k'
    #         row = row + 1
    #         col = col - 1
    #         return row, col, True
    # row + 1, col
    if valid_position(row + 1, col, matrix):
        if next_position(row + 1, col, matrix):
            matrix[row + 1][col] = 'k'
            row = row + 1
            col = col
            return row, col, True
    # row + 1, col + 1
    # if valid_position(row + 1, col + 1, matrix):
    #     if next_position(row + 1, col + 1, matrix):
    #         matrix[row + 1][col + 1] = 'k'
    #         row = row + 1
    #         col = col + 1
    #         return row, col, True
    return row, col, False


number_of_maze = int(input())
matrix = []

# insert matrix
for line in range(number_of_maze):
    matrix.append(list(input()))

# find Katy's position
current_position = []
for row in range(number_of_maze):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'k':
            current_position.append(row)
            current_position.append(col)


# check position around the Katy
row = current_position[0]
col = current_position[1]

count = 0
get_out = False
while True:
    next_row, next_col, get_out = find_next_position(row, col, matrix)
    count += 1
    if get_out:
        row = next_row
        col = next_col
        get_out = False
    else:
        if is_last_move(row, col, matrix, number_of_maze):
            print(f'Kate got out in {count} moves')
            break
        else:
            print('Kate cannot get out')
            break


