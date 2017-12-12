import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        directions = opened_file.read()
    return directions.split(',')

def part_one(directions):
    coordinates = []
    x = 0
    y = 0
    for direction in directions:
        if 'n' == direction:
            y += 2
        elif 'ne' == direction:
            x += 1
            y += 1
        elif 'se' == direction:
            x += 1
            y -= 1
        elif 's' == direction:
            y -= 2
        elif 'sw' == direction:
            x -= 1
            y -= 1
        elif 'nw' == direction:
            x -= 1
            y += 1
        coordinates.append((x, y))
    steps = 0
    while abs(x) != abs(y):
        if y > 0:
            y -= 2
        elif y < 0:
            y += 2
        steps += 1
    return steps + abs(x)

def part_two(directions):
    coordinates = []
    x = 0
    y = 0
    max_x = 0
    max_y = 0
    for direction in directions:
        if 'n' == direction:
            y += 2
        elif 'ne' == direction:
            x += 1
            y += 1
        elif 'se' == direction:
            x += 1
            y -= 1
        elif 's' == direction:
            y -= 2
        elif 'sw' == direction:
            x -= 1
            y -= 1
        elif 'nw' == direction:
            x -= 1
            y += 1
        if abs(x) + abs(y) > abs(max_x) + abs(max_y):
            max_x = x
            max_y = y
        coordinates.append((x, y))
    steps = 0
    while abs(max_x) != abs(max_y):
        if y > 0:
            max_y -= 2
        elif y < 0:
            max_y += 2
        steps += 1
    return steps + abs(max_x)

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    directions = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(directions)
    print part_two(directions)
