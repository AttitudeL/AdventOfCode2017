import os
import re
import math

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def load_input(input_file):
    rule = {}
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        contents = opened_file.readlines()
    for content in contents:
        matcher = re.search('^([.#/]+) => ([.#/]+)$', content)
        key = '\n'.join(matcher.group(1).split('/'))
        value = '\n'.join(matcher.group(2).split('/'))
        rule[key] = value
    return rule
    # relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    # with open(relative_path, 'r') as opened_file:
    #     content = opened_file.read()
    # return content

START_PATTERN = '.#.\n..#\n###'

def rotate(pattern):
    matrix = pattern.split('\n')
    rotated = []
    size = len(matrix)
    for j in range(size):
        row = ''
        for i in range(size - 1, -1, -1):
            row += matrix[i][j]
        rotated.append(row)
    return '\n'.join(rotated)

def flip(pattern):
    matrix = pattern.split('\n')
    flipped = []
    size = len(matrix)
    for i in range(size):
        row = ''
        for j in range(size - 1, -1, -1):
            row += matrix[i][j]
        flipped.append(row)
    return '\n'.join(flipped)

def flip_and_rotate(pattern):
    combination = [pattern]
    for i in range(3):
        combination.append(rotate(combination[-1]))
    combination.append(flip(pattern))
    for i in range(3):
        combination.append(rotate(combination[-1]))
    return combination

def split_up(pattern):
    matrix = pattern.split('\n')
    size = len(matrix)
    splitted = []
    i = 0
    j = 0
    if size % 2 == 0:
        for count in range(size*size/4):
            smaller = []
            smaller.append(matrix[i][j:j+2])
            smaller.append(matrix[i+1][j:j+2])
            splitted.append('\n'.join(smaller))
            j += 2
            if j == size:
                i += 2
                j = 0
        return splitted
    if size % 3 == 0:
        for count in range(size*size/9):
            smaller = []
            smaller.append(matrix[i][j:j+3])
            smaller.append(matrix[i+1][j:j+3])
            smaller.append(matrix[i+2][j:j+3])
            splitted.append('\n'.join(smaller))
            j += 3
            if j == size:
                i += 3
                j = 0
        return splitted

def render(rule, iteration):
    pattern = START_PATTERN
    for i in range(iteration):
        splitted = split_up(pattern)
        combined = []
        size = int(math.sqrt(len(splitted)))
        for s in splitted:
            combination = flip_and_rotate(s)
            for c in combination:
                if c in rule:
                    combined.append(rule[c])
                    break
        chunks = [combined[i:i + size] for i in xrange(0, len(combined), size)]
        matrix = ''
        for chunk in chunks:
            for i in range (len(chunk[0].split('\n'))):
                for element in chunk:
                    matrix += element.split('\n')[i]
                matrix += '\n'
        pattern = matrix.strip()
    return pattern.count('#')

def part_one(rule):
    return render(rule, 5)

def part_two(rule):
    return render(rule, 18)

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    rule = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(rule)
    print part_two(rule)
