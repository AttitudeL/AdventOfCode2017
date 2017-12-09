import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.read()
    return content

def part_one(string):
    while '<' in string:
        si = -1
        ei = -1
        i = 0
        while i < len(string):
            if string[i] == '<' and si == -1:
                si = i
            elif string[i] == '!':
                i += 1
            elif string[i] == '>':
                ei = i
                break
            i += 1
        string = string[:si] + string[ei + 1:]
    string = string.replace(',', '')

    count = 0
    stack = []
    for c in string:
        if c == '{':
            stack.append(c)
        elif c == '}':
            count += len(stack)
            stack.pop()
    return count

def part_two(string):
    count = 0
    garbage = ""
    while '<' in string:
        si = -1
        ei = -1
        i = 0
        while i < len(string):
            if string[i] == '<' and si == -1:
                si = i
            elif string[i] == '!':
                i += 1
            elif string[i] == '>':
                ei = i
                break
            i += 1
        garbage += string[si + 1:ei]
        string = string[:si] + string[ei + 1:]
    i = 0
    while i < len(garbage):
        if garbage[i] == '!':
            i += 2
        else:
            count += 1
            i += 1
    return count

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    string = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(string)
    print part_two(string)
