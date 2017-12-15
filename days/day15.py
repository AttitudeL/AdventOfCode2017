import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    return int(content[0][content[0].rfind(' ') + 1:]), int(content[1][content[1].rfind(' ') + 1:])

MASK = (1 << 16) - 1

def part_one(a_start, b_start):
    judge = 0
    a_prev = a_start
    b_prev = b_start
    for count in range(40000000):
        a_prev = a_prev * 16807 % 2147483647
        b_prev = b_prev * 48271 % 2147483647
        if a_prev & MASK == b_prev & MASK:
            judge += 1
    return judge

def generator_a(a_start):
    pair_count = 5000000
    a_prev = a_start
    while pair_count >= 0:
        a_prev = a_prev * 16807 % 2147483647
        if a_prev % 4 == 0:
            pair_count -= 1
            yield a_prev

def generator_b(b_start):
    pair_count = 5000000
    b_prev = b_start
    while pair_count >= 0:
        b_prev = b_prev * 48271 % 2147483647
        if b_prev % 8 == 0:
            pair_count -= 1
            yield b_prev

def part_two(a_start, b_start):
    judge = 0
    gen_a = generator_a(a_start)
    gen_b = generator_b(b_start)
    while True:
        try:
            if gen_a.next() & MASK == gen_b.next() & MASK:
                judge += 1
        except StopIteration:
            return judge

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    a_start, b_start = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(a_start, b_start)
    print part_two(a_start, b_start)
