import os

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def load_input(input_file):
    matrix = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = int(opened_file.read())
    return content

def part_one(number):
    if number == 0: return 1
    length = 1
    while length * length < number:
        length += 2
    length -= 2
    start = length * length + 1
    count = 0
    while count < 4:
        step = 1
        while step <= length + 2 - 1:
            if (start == number):
                return (length + 2) / 2 + abs((step + 1) - ((length + 2) / 2 + 1))
            start += 1
            step += 1
        count += 1

def part_two(number):
    length = 11
    matrix = []
    i = 0
    while i < length:
        j = 0
        row = []
        while j < length:
            row.append(0)
            j += 1
        i += 1
        matrix.append(row)
    x = length / 2
    y = length / 2
    matrix[x][y] = 1
    size = 3
    level = 0
    while True:
        if x == length - 2 or y == length - 2: break
        y += 1
        step = 1
        while step < size / 2 + 1 + level:
            matrix[x][y] = matrix[x-1][y-1] + matrix[x-1][y] + matrix[x-1][y+1] + matrix[x][y+1] + matrix[x+1][y+1] + matrix[x+1][y] + matrix[x+1][y-1] + matrix[x][y-1]
            x -= 1
            step += 1
        step = 1
        while step < size:
            matrix[x][y] = matrix[x-1][y-1] + matrix[x-1][y] + matrix[x-1][y+1] + matrix[x][y+1] + matrix[x+1][y+1] + matrix[x+1][y] + matrix[x+1][y-1] + matrix[x][y-1]
            y -= 1
            step += 1
        step = 1
        while step < size:
            matrix[x][y] = matrix[x-1][y-1] + matrix[x-1][y] + matrix[x-1][y+1] + matrix[x][y+1] + matrix[x+1][y+1] + matrix[x+1][y] + matrix[x+1][y-1] + matrix[x][y-1]
            x += 1
            step += 1
        step = 1
        while step < size + 1:
            matrix[x][y] = matrix[x-1][y-1] + matrix[x-1][y] + matrix[x-1][y+1] + matrix[x][y+1] + matrix[x+1][y+1] + matrix[x+1][y] + matrix[x+1][y-1] + matrix[x][y-1]
            y += 1
            step += 1
        y -= 1
        size += 2
        level += 1
    for row in matrix:
        for num in row:
            if num > number: return num

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    number = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(number)
    print part_two(number)
