import os
import operator

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    l = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        l = map(int, opened_file.read().split())
    return l

def part_one(l):
    s = []
    c = ''
    count = 0
    while True:
        index, value = max(enumerate(l), key=operator.itemgetter(1))
        l[index] = 0
        i = index + 1
        while value > 0:
            l[i % len(l)] += 1
            value -= 1
            i += 1
        c = ''.join(str(x) for x in l)
        count += 1
        if c in s:
            return count
        else:
            s.append(c)

def part_two(l):
    s = []
    c = ''
    while True:
        index, value = max(enumerate(l), key=operator.itemgetter(1))
        l[index] = 0
        i = index + 1
        while value > 0:
            l[i % len(l)] += 1
            value -= 1
            i += 1
        c = ''.join(str(x) for x in l)
        if c in s:
            break
        else:
            s.append(c)
    return len(s) - s.index(c)

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    l = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(l)
    l = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_two(l)
