import os
import re
import copy
import operator
from collections import deque

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

# Tree solution
class Pipe(object):
    def __init__(self, pipe, next_port):
        self.pipe = pipe
        self.next_port = next_port
        self.pipes = []

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return path

def construct(pipes):
    parent = {}
    root = Pipe((0, 0), 0)
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        next_port = node.next_port
        used_pipes = backtrace(parent, root, node)
        remaining_pipes = [(x, y) for x, y in pipes if x == next_port or y == next_port]
        for used in used_pipes:
            if used.pipe in remaining_pipes:
                remaining_pipes.remove(used.pipe)
        for remaining_pipe in remaining_pipes:
            new_port = 0
            if remaining_pipe[0] == next_port:
                new_port = remaining_pipe[1]
            else:
                new_port = remaining_pipe[0]
            next_node = Pipe(remaining_pipe, new_port)
            parent[next_node] = node
            node.pipes.append(next_node)
            queue.append(next_node)
    return root

def sum_ports(nodes):
    count = 0
    for node in nodes:
        count += node.pipe[0] + node.pipe[1]
    return count

def print_nodes(nodes):
    pipes = []
    for node in nodes:
        pipes.append(node.pipe)
    print pipes

def find_strongest(root):
    parent = {}
    strongest = []
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        if not node.pipes:
            strongest.append(sum_ports(backtrace(parent, root, node)))
        for n in node.pipes:
            parent[n] = node
            queue.append(n)
    return max(strongest)

def find_longest(root):
    parent = {}
    longest = {}
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        if not node.pipes:
            nodes = backtrace(parent, root, node)
            if len(nodes) not in longest:
                longest[len(nodes)] = sum_ports(nodes)
            else:
                longest[len(nodes)] = max(longest[len(nodes)], sum_ports(nodes))
        for n in node.pipes:
            parent[n] = node
            queue.append(n)
    key = max(longest.iteritems(), key=operator.itemgetter(0))[0]
    return longest[key]

def print_nodes(nodes):
    pipes = []
    for node in nodes:
        pipes.append(node.pipe)
    print pipes

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    pipes = load_input(current_file + INPUT_FILE_EXTENSION)
    # print part_one(pipes)
    # print part_two(pipes)
    root = construct(pipes)
    print find_strongest(root)
    print find_longest(root)
