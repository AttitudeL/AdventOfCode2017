import os
import re
from collections import Counter

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def load_input(input_file):
    particles = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        contents = opened_file.readlines()
    for content in contents:
        particle = {}
        matcher = re.search('^p=<([-0-9]+,[-0-9]+,[-0-9]+)>, v=<([-0-9]+,[-0-9]+,[-0-9]+)>, a=<([-0-9]+,[-0-9]+,[-0-9]+)>$', content)
        particle['p'] = map(int, matcher.group(1).split(','))
        particle['v'] = map(int, matcher.group(2).split(','))
        particle['a'] = map(int, matcher.group(3).split(','))
        particles.append(particle)
    return particles

def part_one(particles):
    for tick in range(1000):
        for particle in particles:
            particle['v'][0] += particle['a'][0]
            particle['v'][1] += particle['a'][1]
            particle['v'][2] += particle['a'][2]
            particle['p'][0] += particle['v'][0]
            particle['p'][1] += particle['v'][1]
            particle['p'][2] += particle['v'][2]
    positions = []
    for particle in particles:
        positions.append(abs(particle['p'][0]) + abs(particle['p'][1]) + abs(particle['p'][2]))
    return positions.index(min(positions))

def collisions_indices(positions):
    indices = []
    counter= Counter(positions)
    collisions = [position for position in counter.keys() if counter[position] > 1]
    for index, value in enumerate(positions):
        if value in collisions:
            indices.append(index)
    return indices

def part_two(particles):
    for tick in range(1000):
        positions = []
        for particle in particles:
            particle['v'][0] += particle['a'][0]
            particle['v'][1] += particle['a'][1]
            particle['v'][2] += particle['a'][2]
            particle['p'][0] += particle['v'][0]
            particle['p'][1] += particle['v'][1]
            particle['p'][2] += particle['v'][2]
            positions.append((particle['p'][0], particle['p'][1], particle['p'][2]))
        indices = collisions_indices(positions)
        deletes = []
        for index in indices:
            deletes.append(particles[index])
        for delete in deletes:
            particles.remove(delete)
    return len(particles)

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    print part_one(load_input(current_file + INPUT_FILE_EXTENSION))
    print part_two(load_input(current_file + INPUT_FILE_EXTENSION))
