import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.read()
    return content

def get_list(size):
    l = []
    i = 0
    while i < size:
        l.append(i)
        i += 1
    return l

def part_one(l, ll):
    l = map(int, l.split(','))
    index = 0
    skip_size = 0
    for length in l:
        if length <= len(ll):
            i = 0
            rev = []
            while i < length:
                rev.append(ll[(index + i) % len(ll)])
                i += 1
            rev = list(reversed(rev))
            i = 0
            while i < length:
                ll[(index + i) % len(ll)] = rev[i]
                i += 1
            index += length + skip_size
            skip_size += 1
        else:
            continue
    return ll[0] * ll[1]

def part_two(l, ll):
    lm = []
    for e in l:
        lm.append(ord(str(e)))
    lm.extend([17, 31, 73, 47, 23])
    l = lm

    index = 0
    skip_size = 0
    count = 0
    while count < 64:
        for length in l:
            i = 0
            rev = []
            while i < length:
                rev.append(ll[(index + i) % len(ll)])
                i += 1
            rev = list(reversed(rev))
            i = 0
            while i < length:
                ll[(index + i) % len(ll)] = rev[i]
                i += 1
            index += length + skip_size
            skip_size += 1
        count += 1
    ll = [ll[i:i + 16] for i in xrange(0, len(ll), 16)]
    lll = []
    for chunk in ll:
        lll.append(reduce(lambda x, y: x^y, chunk))
    result = ""
    for d in lll:
        h = hex(d).replace('0x', '')
        if len(h) == 1:
            h = '0' + h
        result += h
    return result

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    l = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(l, get_list(256))
    print part_two(l, get_list(256))
