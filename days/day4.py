import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    matrix = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    for line in content:
        matrix.append(line.split())
    return matrix

def part_one(matrix):
    count = 0
    for row in matrix:
        container = []
        valid = True
        for password in row:
            if password in container:
                valid = False
                break
            else:
                container.append(password)
        if valid: count += 1
    return count

def part_two(matrix):
    count = 0
    for row in matrix:
        container = []
        valid = True
        for password in [''.join(sorted(i)) for i in row]:
            if password in container:
                valid = False
                break
            else:
                container.append(password)
        if valid: count += 1
    return count

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    matrix = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(matrix)
    print part_two(matrix)
