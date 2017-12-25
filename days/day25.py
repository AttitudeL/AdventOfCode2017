import os

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def move_right(tape, index):
    new_index = index + 1
    if new_index >= len(tape):
        tape.append(0)
    return new_index

def move_left(tape, index):
    new_index = index - 1
    if new_index < 0:
        tape.insert(0, 0)
        return 0
    return new_index

"""
Respect Turing!
"""
def turing_machine():
    tape = [0]
    index = 0
    state = 'A'
    for i in range(12261543):
        if state == 'A':
            if tape[index] == 0:
                tape[index] = 1
                index = move_right(tape, index)
                state = 'B'
                continue
            if tape[index] == 1:
                tape[index] = 0
                index = move_left(tape, index)
                state = 'C'
                continue
        if state == 'B':
            if tape[index] == 0:
                tape[index] = 1
                index = move_left(tape, index)
                state = 'A'
                continue
            if tape[index] == 1:
                tape[index] = 1
                index = move_right(tape, index)
                state = 'C'
                continue
        if state == 'C':
            if tape[index] == 0:
                tape[index] = 1
                index = move_right(tape, index)
                state = 'A'
                continue
            if tape[index] == 1:
                tape[index] = 0
                index = move_left(tape, index)
                state = 'D'
                continue
        if state == 'D':
            if tape[index] == 0:
                tape[index] = 1
                index = move_left(tape, index)
                state = 'E'
                continue
            if tape[index] == 1:
                tape[index] = 1
                index = move_left(tape, index)
                state = 'C'
                continue
        if state == 'E':
            if tape[index] == 0:
                tape[index] = 1
                index = move_right(tape, index)
                state = 'F'
                continue
            if tape[index] == 1:
                tape[index] = 1
                index = move_right(tape, index)
                state = 'A'
                continue
        if state == 'F':
            if tape[index] == 0:
                tape[index] = 1
                index = move_right(tape, index)
                state = 'A'
                continue
            if tape[index] == 1:
                tape[index] = 1
                index = move_right(tape, index)
                state = 'E'
                continue
    return tape.count(1)

if __name__ == '__main__':
    print turing_machine()
