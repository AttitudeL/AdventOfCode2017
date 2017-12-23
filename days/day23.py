import os

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def get_val(string):
    try:
        return int(string)
    except ValueError:
        return string

def load_input(input_file):
    instructions = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        contents = opened_file.readlines()
    for content in contents:
        splited = content.strip().split()
        instructions.append((splited[0], get_val(splited[1]), get_val(splited[2])))
    return instructions

def get(registers, value):
    if isinstance(value, int):
        return value
    elif isinstance(value, str):
        return registers[value]

def part_one(instructions):
    registers = {}
    count = 0
    index = 0
    while index < len(instructions):
        operator = instructions[index][0]
        register = instructions[index][1]
        value = instructions[index][2]
        if register not in registers:
            registers[register] = 0
        if operator == 'set':
            registers[register] = get(registers, value)
        if operator == 'sub':
            registers[register] -= get(registers, value)
        if operator == 'mul':
            registers[register] *= get(registers, value)
            count += 1
        if operator == 'jnz':
            if get(registers, register) != 0:
                index += get(registers, value)
                continue
        index += 1
    return count

def part_two(instructions):
    registers = {}
    registers['a'] = 1
    index = 0
    while index < 8:
        operator = instructions[index][0]
        register = instructions[index][1]
        value = instructions[index][2]
        if register not in registers:
            registers[register] = 0
        if operator == 'set':
            registers[register] = get(registers, value)
        if operator == 'sub':
            registers[register] -= get(registers, value)
        if operator == 'mul':
            registers[register] *= get(registers, value)
        if operator == 'jnz':
            if get(registers, register) != 0:
                index += get(registers, value)
                continue
        index += 1
    
    b = registers['b']
    c = registers['c']
    h = 0
    """
    Original Program Translation
    while b <= c:
        f = 1
        d = 2
        e = 2
        while d < b:
            while e < b:
                if d * e == b:
                    f = 0
                e += 1
        d += 1
        if f == 0:
            h += 1
        b += 17
    """
    while b <= c:
        e = 2
        while e < b:
            if b % e == 0:
                h += 1
                break
            e += 1
        b += 17
    return h

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    instructions = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(instructions)
    print part_two(instructions)
