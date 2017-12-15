import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    scanners = {}
    max_layer = 0
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        lines = opened_file.readlines()
    for line in lines:
        layer = int(line[:line.find(':')])
        scanner_range = int(line[line.find(':') + 1:])
        scanners[layer] = (scanner_range, 0)
        max_layer = max(max_layer, layer)
    for layer in range(max_layer):
        if layer not in scanners:
            scanners[layer] = None
    return scanners

def is_at_top(step, scanner_range):
    return step % (scanner_range * 2 - 2) == 0

def part_one(scanners):
    severity = 0
    for step, layer in enumerate(scanners):
        if scanners[layer] is not None and is_at_top(step, scanners[layer][0]):
            severity +=  layer * scanners[layer][0]
    return severity

def part_two(scanners):
    delay = 0
    while True:
        if is_at_top(delay, scanners[0][0]):
           delay += 1
           continue
        step = delay
        caught = False
        for layer in scanners:
            if scanners[layer] is not None and is_at_top(step, scanners[layer][0]):
                caught = True
                break
            step += 1
        if not caught:
            return delay
        delay += 1
    return delay

if __name__ == "__main__":
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    scanners = load_input(current_file + INPUT_FILE_EXTENSION)
    print part_one(scanners)
    print part_two(scanners)
