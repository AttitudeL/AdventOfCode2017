import os

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def load_input(input_file):
    matrix = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        contents = opened_file.readlines()
    for content in contents:
        matrix.append(content.rstrip())
    return matrix

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get(matrix, i, j):
    if i >= 0 and i < len(matrix) and j >= 0 and j <len(matrix[i]):
        return matrix[i][j]
    else:
        return ' '

def part_one(matrix):
    letters = ''
    i = 1
    j = matrix[0].find('|')
    direction = 'down'
    while True:
        if matrix[i][j] == ' ':
            return letters
        if matrix[i][j] == '+':
            up = get(matrix, i - 1, j)
            down = get(matrix, i + 1, j)
            left = get(matrix, i, j - 1)
            right = get(matrix, i, j + 1)
            if direction == 'up' or direction == 'down':
                if right != ' ':
                    direction = 'right'
                    j += 1
                elif left != ' ':
                    direction = 'left'
                    j -= 1
            elif direction == 'left' or direction == 'right':
                if up != ' ':
                    direction = 'up'
                    i -= 1
                elif down != ' ':
                    direction = 'down'
                    i += 1
            continue
        if matrix[i][j] in LETTERS:
            letters += matrix[i][j]
        if direction == 'up':
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'right':
            j += 1
        elif direction == 'left':
            j -= 1

def part_two(matrix):
    steps = 0
    i = 1
    j = matrix[0].find('|')
    direction = 'down'
    while True:
        steps += 1
        if matrix[i][j] == ' ':
            return steps
        if matrix[i][j] == '+':
            up = get(matrix, i - 1, j)
            down = get(matrix, i + 1, j)
            left = get(matrix, i, j - 1)
            right = get(matrix, i, j + 1)
            if direction == 'up' or direction == 'down':
                if right != ' ':
                    direction = 'right'
                    j += 1
                elif left != ' ':
                    direction = 'left'
                    j -= 1
            elif direction == 'left' or direction == 'right':
                if up != ' ':
                    direction = 'up'
                    i -= 1
                elif down != ' ':
                    direction = 'down'
                    i += 1
            continue
        if direction == 'up':
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'right':
            j += 1
        elif direction == 'left':
            j -= 1

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    matrix = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(matrix)
    print part_two(matrix)
