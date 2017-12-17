import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        steps = int(opened_file.read())
    return steps

def part_one(steps):
    buffer = [0]
    while len(buffer) <= 2018:
        current_value = len(buffer) - 1
        buffer.insert((buffer.index(current_value) + steps) % len(buffer) + 1, current_value + 1)
    return buffer[buffer.index(2017) + 1]

def part_two(steps):
    """
    Unless part one, we already know the index (the index is 1, which is after value 0) of this part.
    Therefore, we can keep track of the index of the value after every insert.
    If this index is happen to be at index 1, we record this value.
    Once the iteration is over, we will have the result, i.e. the last value we have recored so far.
    This way we don't need to keep a list in memory and actually inserting value after each iteration.
    """
    result = 0
    insert_index = 0
    buffer_size = 1
    while buffer_size <= 50000000:
        insert_index = (insert_index + steps) % buffer_size + 1
        if insert_index == 1:
            result = buffer_size
        buffer_size += 1
    return result

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    steps = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(steps)
    print part_two(steps)
