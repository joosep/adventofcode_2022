# https://adventofcode.com/2022/day/3

def has_full_overlap(f1, l1, f2, l2):
    f1, l1, f2, l2 = int(f1), int(l1), int(f2), int(l2)
    return f1 >= f2 and l1 <= l2 or f1 <= f2 and l1 >= l2


def has_overlap(f1, l1, f2, l2):
    f1, l1, f2, l2 = int(f1), int(l1), int(f2), int(l2)
    return f2 <= f1 <= l2 or f2 <= l1 <= l2 or f1 <= f2 <= l1 or f1 <= l2 <= l1


def calc_part1(input_file):
    with open(input_file) as f:
        return sum(has_full_overlap(*line.replace('-', ',').split(',')) for line in f.read().splitlines())


def calc_part2(input_file):
    with open(input_file) as f:
        return sum(has_overlap(*line.replace('-', ',').split(',')) for line in f.read().splitlines())


assert calc_part1('test_data') == 2

print(f'answer: {calc_part1("input_data")}')

assert calc_part2('test_data') == 4

print(f'answer: {calc_part2("input_data")}')
