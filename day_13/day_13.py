# https://adventofcode.com/2022/day/13

import json
from functools import cmp_to_key


def read_input(data):
    converted_packages = []
    for packages in [packages.split('\n') for packages in open(data).read().split('\n\n')]:
        converted_packages.append((json.loads(packages[0]), json.loads(packages[1])))
    return converted_packages


def compare_lists(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    if isinstance(left, list) and isinstance(right, list):
        for i in range(0, min(len(left), len(right))):
            order = compare_lists(left[i], right[i])
            if order != 0:
                return order
        return len(left) - len(right)
    if isinstance(left, int):
        return compare_lists([left], right)
    if isinstance(right, int):
        return compare_lists(left, [right])


def get_part1(data):
    packages = read_input(data)
    in_order_sum = 0
    for i in range(0, len(packages)):
        in_order_sum += i + 1 if compare_lists(*packages[i]) < 0 else 0
    return in_order_sum


def get_part2(data):
    packages = [list for t in read_input(data) for list in t]
    packages.append([[2]])
    packages.append([[6]])
    packages = sorted(packages, key=cmp_to_key(compare_lists))
    decode_key = 1
    for i in range(0, len(packages)):
        decode_key *= i + 1 if packages[i] == [[2]] or packages[i] == [[6]] else 1
    return decode_key


result = get_part1("test_data")
assert result == 13, f"got: {result}"

result = get_part1("input_data")
assert result == 5185, f"got: {result}"

result = get_part2("test_data")
assert result == 140, f"got: \n{result}"

result = get_part2("input_data")
assert result == 23751, f"got: \n{result}"
