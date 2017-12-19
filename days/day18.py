import os
import collections
import multiprocessing.pool
from multiprocessing import Queue

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
        if len(splited) == 2:
            instructions.append((splited[0], get_val(splited[1])))
        elif len(splited) == 3:
            instructions.append((splited[0], get_val(splited[1]), get_val(splited[2])))
    return instructions

def part_one(instructions):
    registers = {}
    last_frequency = 0
    index = 0
    while True:
        operator = instructions[index][0]
        register = instructions[index][1]
        if register not in registers:
            registers[register] = 0
        if operator == 'snd':
            last_frequency = get(registers, register)
        elif operator == 'set':
            registers[register] = get(registers, instructions[index][2])
        elif operator == 'add':
            registers[register] += get(registers, instructions[index][2])
        elif operator == 'mul':
            registers[register] *= get(registers, instructions[index][2])
        elif operator == 'mod':
            registers[register] %= get(registers, instructions[index][2])
        elif operator == 'rcv':
            if registers[register] != 0:
                return last_frequency
        elif operator == 'jgz':
            if registers[register] > 0:
                index += get(registers, instructions[index][2])
                continue
        index += 1

def get(registers, value):
    if isinstance(value, int):
        return value
    elif isinstance(value, str):
        return registers[value]

def program(id, instructions, state, queue_self, queue_other):
    registers = collections.defaultdict(int)
    registers['p'] = id
    send_count = 0
    index = 0
    while index < len(instructions):
        cmd = instructions[index][0]
        register = instructions[index][1]
        if cmd == 'snd':
            queue_self.put(get(registers, register))
            state[id] = True
            send_count += 1
        elif cmd == 'set':
            registers[register] = get(registers, instructions[index][2])
        elif cmd == 'add':
            registers[register] += get(registers, instructions[index][2])
        elif cmd == 'mul':
            registers[register] *= get(registers, instructions[index][2])
        elif cmd == 'mod':
            registers[register] %= get(registers, instructions[index][2])
        elif cmd == 'rcv':
            value = queue_other.get()
            if value == 'end':
                return send_count
            else:
                registers[register] = value
        elif cmd == 'jgz':
            if get(registers, register) > 0:
                index += get(registers, instructions[index][2])
                continue
        index += 1
    return send_count

def preempt(state, q0, q1):
    """
    Preemption technique
    * Wait for both programs to send before trigging preemption
    * Wait for both programs queue to be empty so they are both blocked and then send 'end' to each queue to preempt them
    """
    while not state[0] or not state[1]:
        pass
    while not q0.empty() or not q1.empty():
        pass
    q0.put('end')
    q1.put('end')

def part_two(instructions):
    q0 = multiprocessing.Queue()
    q1 = multiprocessing.Queue()
    state = [False, False]
    pool = multiprocessing.pool.ThreadPool(processes=3)
    thread_0 = pool.apply_async(program, (0, instructions, state, q0, q1))
    thread_1 = pool.apply_async(program, (1, instructions, state, q1, q0))
    preemption = pool.apply_async(preempt, (state, q0, q1))
    result_0 = thread_0.get()
    result_1 = thread_1.get()
    preemption.get()
    return result_1

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    instructions = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(instructions)
    print part_two(instructions)
