# https://adventofcode.com/2022/day/3
def letter_to_num(e):
    return ord(e) - 96 if ord(e) > 90 else ord(e) - 38


def calc_part1(input_file):
    shared_items = []
    with open(input_file) as f:
        for line in f.read().splitlines():
            half = len(line) // 2
            duplicates = set(e for e in line[:half] if e in line[half:])
            shared_items.extend(duplicates)
    return sum(letter_to_num(e) for e in shared_items)


def calc_part2(input_file):
    shared_items = []
    with open(input_file) as f:
        for group in zip(*(iter(f.read().splitlines()),) * 3):
            duplicates = set(e for e in group[0] if e in group[1] and e in e in group[2])
            shared_items.extend(duplicates)
    return sum(letter_to_num(e) for e in shared_items)


assert calc_part1('test_data') == 157

print(f'answer: {calc_part1("input_data")}')

assert calc_part2('test_data') == 70

print(f'answer: {calc_part2("input_data")}')
