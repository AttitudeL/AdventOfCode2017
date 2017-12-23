import os

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def load_input(input_file):
    matrix = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        contents = opened_file.readlines()
    for content in contents:
        matrix.append(content.strip())
    return matrix

def expand_matrix(matrix):
    expanded = []
    expanded.append('.' * (len(matrix) + 2))
    for row in matrix:
        expanded.append('.' + row + '.')
    expanded.append('.' * (len(matrix) + 2))
    return expanded

def split_up(matrix):
    splitted = []
    for row in matrix:
        splitted.append(list(row))
    return splitted

def combine(splitted):
    matrix = []
    for row in splitted:
        matrix.append(''.join(row))
    return matrix

def move(i, j, current_direction, pending_direction):
    if current_direction == 'up':
        if pending_direction == 'right':
            return i, j + 1, 'right'
        if pending_direction == 'left':
            return i, j - 1, 'left'
        if pending_direction == 'forward':
            return i - 1, j, 'up'
        if pending_direction == 'reverse':
            return i + 1, j, 'down'
    if current_direction == 'right':
        if pending_direction == 'right':
            return i + 1, j, 'down'
        if pending_direction == 'left':
            return i - 1, j, 'up'
        if pending_direction == 'forward':
            return i, j + 1, 'right'
        if pending_direction == 'reverse':
            return i, j - 1, 'left'
    if current_direction == 'down':
        if pending_direction == 'right':
            return i, j - 1, 'left'
        if pending_direction == 'left':
            return i, j + 1, 'right'
        if pending_direction == 'forward':
            return i + 1, j, 'down'
        if pending_direction == 'reverse':
            return i - 1, j, 'up'
    if current_direction == 'left':
        if pending_direction == 'right':
            return i - 1, j, 'up'
        if pending_direction == 'left':
            return i + 1, j, 'down'
        if pending_direction == 'forward':
            return i, j - 1, 'left'
        if pending_direction == 'reverse':
            return i, j + 1, 'right'

def part_one(matrix, iteration):
    splitted = split_up(matrix)
    infected = 0
    i, j = len(matrix) / 2, len(matrix) / 2
    current_direction = 'up'
    for count in range(iteration):
        pending_direction = ''
        if splitted[i][j] == '#':
            pending_direction = 'right'
        else:
            pending_direction = 'left'
        if splitted[i][j] == '.':
            splitted[i][j] = '#'
            infected += 1
        else:
            splitted[i][j] = '.'
        i, j, current_direction = move(i, j, current_direction, pending_direction)
        if i < 0 or i >= len(splitted) or j < 0 or j >= len(splitted):
            combined = expand_matrix(combine(splitted))
            splitted = split_up(combined)
            i += 1
            j += 1
    return infected

def part_two(matrix, iteration):
    splitted = split_up(matrix)
    infected = 0
    i, j = len(matrix) / 2, len(matrix) / 2
    current_direction = 'up'
    for count in range(iteration):
        pending_direction = ''
        if splitted[i][j] == '.':
            pending_direction = 'left'
            splitted[i][j] = 'W'
        elif splitted[i][j] == 'W':
            pending_direction = 'forward'
            splitted[i][j] = '#'
            infected += 1
        elif splitted[i][j] == '#':
            pending_direction = 'right'
            splitted[i][j] = 'F'
        elif splitted[i][j] == 'F':
            pending_direction = 'reverse'
            splitted[i][j] = '.'
        i, j, current_direction = move(i, j, current_direction, pending_direction)
        if i < 0 or i >= len(splitted) or j < 0 or j >= len(splitted):
            combined = expand_matrix(combine(splitted))
            splitted = split_up(combined)
            i += 1
            j += 1
    return infected

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    matrix = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(matrix, 10000)
    print part_two(matrix, 10000000)
