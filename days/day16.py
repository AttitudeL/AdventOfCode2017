import os

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def load_input(input_file):
    moves = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        instructions = opened_file.read().split(',')
    for instruction in instructions:
        first_char = instruction[0]
        if first_char == 's':
            moves.append(('s', int(instruction[1:])))
        elif first_char == 'x':
            moves.append(('x', int(instruction[1:instruction.find('/')]), int(instruction[instruction.find('/') + 1:])))
        elif first_char == 'p':
            moves.append(('p', instruction[1:instruction.find('/')], instruction[instruction.find('/') + 1:]))
    return moves

def dance(moves, program):
    for move in moves:
        if move[0] == 's':
            program = program[-move[1]:] + program[:-move[1]]
        elif move[0] == 'x':
            char = program[move[1]]
            program[move[1]] = program[move[2]]
            program[move[2]] = char
        elif move[0] == 'p':
            index_a = program.index(move[1])
            index_b = program.index(move[2])
            char = program[index_a]
            program[index_a] = program[index_b]
            program[index_b] = char
    return program

def stringfy(program):
    return ''.join(program)

def part_one(moves, program):
    program = dance(moves, program)
    return stringfy(program)

def part_two(moves, program):
    encountered = []
    count = 0
    while True:
        program = dance(moves, program)
        count += 1
        # if found one encounter, we can calculate the cycle for this repeated encounter and skip these cycles
        if stringfy(program) in encountered:
            start_index = encountered.index(stringfy(program))
            end_index = len(encountered)
            for index in range((1000000000 - count) % (end_index - start_index)):
                program = dance(moves, program)
            return stringfy(program)
        else:
            encountered.append(stringfy(program))

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    moves = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(moves, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
    print part_two(moves, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
