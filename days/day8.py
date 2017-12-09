import os
import operator

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    l = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    for line in content:
        sp = line.split()
        fi = sp[0]
        if sp[1] == 'inc':
            op = operator.add
        elif sp[1] == 'dec':
            op = operator.sub
        fn = int(sp[2])
        si = sp[4]
        cond = sp[5]
        sn = int(sp[6])
        l.append((fi, op, fn, si, cond, sn))
    return l

def compare(n1, op, n2):
    if op == '>': return n1 > n2
    if op == '>=': return n1 >= n2
    if op == '<': return n1 < n2
    if op == '<=': return n1 <= n2
    if op == '==': return n1 == n2
    if op == '!=': return n1 != n2

def part_one(l):
    d = {}
    for ins in l:
        if ins[0] not in d: d[ins[0]] = 0
        if ins[3] not in d: d[ins[3]] = 0
        if compare(d[ins[3]], ins[4], ins[5]):
            d[ins[0]] = ins[1](d[ins[0]], ins[2])
    return max(d.iteritems(), key=operator.itemgetter(1))[1]

def part_two(l):
    largest = 0
    d = {}
    for ins in l:
        if ins[0] not in d: d[ins[0]] = 0
        if ins[3] not in d: d[ins[3]] = 0
        if compare(d[ins[3]], ins[4], ins[5]):
            d[ins[0]] = ins[1](d[ins[0]], ins[2])
            largest = max(largest, d[ins[0]])
    return largest

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    l = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(l)
    print part_two(l)
