import os
import re
import copy
import operator

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def load_input(input_file):
    ports = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        contents = opened_file.readlines()
    for content in contents:
        matcher = re.search('^([0-9]+)/([0-9]+)$', content)
        ports.append((int(matcher.group(1)), int(matcher.group(2))))
    return ports

def sum_up(pipes):
    count = 0
    for pipe in pipes:
        count += pipe[0] + pipe[1]
    return count

def get_port(port, pipe):
    if pipe[0] == port:
        return pipe[1]
    else:
        return pipe[0]

def get_pipes(pipes, pipe):
    new_pipes = []
    new_pipes.extend(pipes)
    new_pipes.append(pipe)
    return new_pipes

def get_rest(rest, pipes):
    return list(set(rest) - set(pipes))

def strongest(port, pipes, rest):
    remaining = set([(x, y) for x, y in rest if x == port or y == port]) - set(pipes)
    bridges = []
    if not remaining:
        return sum_up(pipes)
    for pipe in remaining:
        new_port = get_port(port, pipe)
        new_pipes = get_pipes(pipes, pipe)
        new_rest = get_rest(rest, new_pipes)
        bridges.append(strongest(new_port, new_pipes, new_rest))
    return max(bridges)

def longest(port, pipes, rest, map):
    remaining = set([(x, y) for x, y in rest if x == port or y == port]) - set(pipes)
    if not remaining:
        if len(pipes) in map:
            map[len(pipes)] = max(map[len(pipes)], sum_up(pipes))
        else:
            map[len(pipes)] = sum_up(pipes)
        return
    for pipe in remaining:
        new_port = get_port(port, pipe)
        new_pipes = get_pipes(pipes, pipe)
        new_rest = get_rest(rest, new_pipes)
        longest(new_port, new_pipes, new_rest, map)

def part_one(pipes):
    bridges = []
    start_ports = [(x, y) for x, y in pipes if x == 0 or y == 0]
    for port in start_ports:
        bridges.append(strongest(port[1], [port], copy.deepcopy(pipes)))
    return max(bridges)

def part_two(currenpipest_file):
    map = {}
    start_ports = [(x, y) for x, y in pipes if x == 0 or y == 0]
    for port in start_ports:
        longest(port[1], [port], copy.deepcopy(pipes), map)
    key = max(map.iteritems(), key=operator.itemgetter(0))[0]
    return map[key]

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    pipes = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(pipes)
    print part_two(pipes)
