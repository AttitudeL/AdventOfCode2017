import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    matrix = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    for line in content:
        matrix.append(map(int, line.split()))
    return matrix

def part_one(matrix):
    result = []
    for row in matrix:
        result.append(max(row) - min(row))
    print sum(result)

def part_two(matrix):
    result = []
    for row in matrix:
        i = 0
        while i < len(row):
            j = i + 1
            while j < len(row):
                if max(row[i], row[j]) % min(row[i], row[j]) == 0:
                    result.append(max(row[i], row[j]) / min(row[i], row[j]))
                j += 1
            i += 1
    print sum(result)

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    matrix = load_input(current_file + INPUT_FILE_EXTENSION)
    part_one(matrix)
    part_two(matrix)
