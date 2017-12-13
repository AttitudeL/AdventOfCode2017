import os
from collections import deque

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    ids = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        lines = opened_file.readlines()
    for line in lines:
        line = line.strip()
        id = int(line[:line.find('<')])
        link = map(int, line[line.find('>') + 1:].split(','))
        ids.append((id, link))
    return ids

def part_one(ids):
    id_maps = {}
    for id in ids:
        if id[0] not in id_maps:
            id_maps[id[0]] = set()
        for linked_id in id[1]:
            id_maps[id[0]].add(linked_id)
            if linked_id not in id_maps:
                id_maps[linked_id] = set()
            id_maps[linked_id].add(id[0])
    result = set()
    queue = deque()
    popped = []
    for id in id_maps[0]:
        queue.append(id)
    while len(queue) > 0:
        id = queue.popleft()
        if id in popped:
            continue
        else:
            popped.append(id)
        result.add(id)
        for linked_id in id_maps[id]:
            queue.append(linked_id)
    return len(result)

def part_two(ids):
    id_maps = {}
    for id in ids:
        if id[0] not in id_maps:
            id_maps[id[0]] = set()
        for linked_id in id[1]:
            id_maps[id[0]].add(linked_id)
            if linked_id not in id_maps:
                id_maps[linked_id] = set()
            id_maps[linked_id].add(id[0])
    group = []
    for id_map in id_maps:
        result = set()
        queue = deque()
        popped = []
        for id in id_maps[id_map]:
            queue.append(id)
        while len(queue) > 0:
            id = queue.popleft()
            if id in popped:
                continue
            else:
                popped.append(id)
            result.add(id)
            for linked_id in id_maps[id]:
                queue.append(linked_id)
        if sorted(result) not in group:
            group.append(sorted(result))
    return len(group)

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    ids = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(ids)
    print part_two(ids)
