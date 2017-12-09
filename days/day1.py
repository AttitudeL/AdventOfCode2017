import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        input = opened_file.read()
    return input, len(input)

def part_one(input, length):
    result = []
    index = 0
    while index <= length:
        if (input[index % length] == input[(index + 1) % length]):
            result.append(int(input[index % length]))
        index += 1
    print sum(result)

def part_two(input, length):
    result = []
    index = 0
    while index <= length:
        if (input[index % length] == input[(index + length / 2) % length]):
            result.append(int(input[index % length]))
        index += 1
    print sum(result)

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    input, length = load_input(current_file + INPUT_FILE_EXTENSION)
    part_one(input, length)
    part_two(input, length)
