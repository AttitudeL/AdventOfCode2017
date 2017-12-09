import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    l = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    for line in content:
        l.append(int(line))
    return l

def part_one(l):
    i = 0
    steps = 0
    while True:
        if i < 0 or i >= len(l):
            return steps
        j = i
        i += l[i]
        l[j] += 1
        steps += 1

def part_two(l):
    i = 0
    steps = 0
    while True:
        if i < 0 or i >= len(l):
            return steps
        j = i
        i += l[i]
        if l[j] >= 3:
            l[j] -= 1
        else:
            l[j] += 1
        steps += 1

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    l1 = load_input(current_file + INPUT_FILE_EXTENSION)
    l2 = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(l1)
    print part_two(l2)
