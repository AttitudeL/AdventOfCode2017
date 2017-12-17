import os
import binascii
from collections import deque

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def load_input(input_file):
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.read()
    return content

def knot_hash(input):
    hash_list = []
    for digit in range(256):
        hash_list.append(digit)

    ascii_list = []
    for char in input:
        ascii_list.append(ord(str(char)))
    ascii_list.extend([17, 31, 73, 47, 23])

    index = 0
    skip_size = 0
    count = 0
    for count in range(64):
        for ascii_digit in ascii_list:
            reversed_list = []
            for digit in range(ascii_digit):
                reversed_list.append(hash_list[(index + digit) % 256])
            reversed_list = list(reversed(reversed_list))
            for digit in range(ascii_digit):
                hash_list[(index + digit) % 256] = reversed_list[digit]
            index += ascii_digit + skip_size
            skip_size += 1
    
    hash_list = [hash_list[i:i + 16] for i in xrange(0, 256, 16)]
    hex_list = []
    for hash_chunk in hash_list:
        hex_list.append(reduce(lambda x, y: x^y, hash_chunk))
    result = ''
    for hex_chunk in hex_list:
        hex_string = hex(hex_chunk).replace('0x', '')
        if len(hex_string) == 1:
            result += '0' + hex_string
        else:
            result += hex_string
    return result

def byte_to_binary(byte):
    return ''.join(str((byte & (1 << i)) and 1) for i in reversed(range(8)))

def hex_to_binary(hex):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(hex))

def part_one(input):
    raw_list = []
    for index in range(128):
        raw_list.append(input + '-' + str(index))
    matrix = []
    for raw in raw_list:
        matrix.append([int(x) for x in hex_to_binary(knot_hash(raw))])
    count = 0
    for row in matrix:
        count += row.count(1)
    return count

def get(matrix, i, j):
    if i < 0 or i > 127:
        return None
    if j < 0 or j > 127:
        return None
    return matrix[i][j]

def part_two(input):
    raw_list = []
    for index in range(128):
        raw_list.append(input + '-' + str(index))
    matrix = []
    for raw in raw_list:
        matrix.append([x for x in hex_to_binary(knot_hash(raw))])

    square_locations = []
    for i in range(128):
        for j in range(128):
            if matrix[i][j] == '1':
                square_locations.append((i,j))
    
    current_region = 1
    index = 0
    while len(square_locations) > 0:
        i = square_locations[index][0]
        j = square_locations[index][1]
        queue = deque()
        queue.append((i, j))
        while len(queue) > 0:
            offset = queue.popleft()
            x = offset[0]
            y = offset[1]
            if matrix[x][y] == '1':
                matrix[x][y] = current_region
                square_locations.remove((x, y))
            if get(matrix, x - 1, y) == '1':
                queue.append((x - 1, y))
            if get(matrix, x + 1, y) == '1':
                queue.append((x + 1, y))
            if get(matrix, x, y - 1) == '1':
                queue.append((x, y - 1))
            if get(matrix, x, y + 1) == '1':
                queue.append((x, y + 1))
        current_region += 1
    return current_region - 1

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    input = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(input)
    print part_two(input)
