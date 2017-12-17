import os
import copy

INPUT_DIRECTORY = '../inputs/'
INPUT_FILE_EXTENSION = '_input.txt'

def load_input(input_file):
    d = {}
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    for l in content:
        name = l[:l.find(' ')]
        weight = int(l[l.find('(') + 1:l.find(')')])
        if '->' in l:
            link = [x.strip() for x in l[l.find('->') + 2:].split(',')]
        else:
            link = None
        d[name] = (weight, link)
    return d

def part_one(tower):
    l1 = []
    l2 = []
    for t in tower.keys():
        l1.append(t)
    for t in tower.keys():
        if tower[t][1] is not None:
            l2.extend(tower[t][1])
    return list(set(l1) - set(l2))[0]

def part_two(tower):
    original = copy.deepcopy(tower)
    while True:
        tbd = []
        modified = []
        for t in tower.keys():
            if tower[t][1] is not None:
                subs = []
                weights = []
                bottom_level = True
                for sub in tower[t][1]:
                    if tower[sub][1] is not None:
                        bottom_level = False
                    else:
                        subs.append(sub)
                        weights.append(tower[sub][0])
                if bottom_level:
                    if not all(x == weights[0] for x in weights):
                        delta = max(weights) - min(weights)
                        for t in subs:
                            if tower[t][0] == max(weights):
                                return original[t][0] - delta
                    else:
                        tbd.extend(subs)
                        tower[t] = (tower[t][0] + sum(weights), tower[t][1])
                        modified.append(t)
        for t in tbd:
            del tower[t]
        for t in modified:
            tower[t] = (tower[t][0], None)

if __name__ == '__main__':
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    towers = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(towers)
    print part_two(towers)
