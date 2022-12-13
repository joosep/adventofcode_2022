# https://adventofcode.com/2022/day/13

import json


def read_input(data):
    converted_packages = []
    for packages in [packages.split('\n') for packages in open(data).read().split('\n\n')]:
        converted_packages.append((json.loads(packages[0]), json.loads(packages[1])))
    return converted_packages


def is_in_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if right < left:
            return False
        return None
    if isinstance(left, list) and isinstance(right, list):
        for i in range(0, min(len(left), len(right))):
            order = is_in_order(left[i], right[i])
            if order is not None:
                return order
        if len(left) < len(right):
            return True
        if len(right) < len(left):
            return False
        return None
    if isinstance(left, int):
        return is_in_order([left], right)
    if isinstance(right, int):
        return is_in_order(left, [right])


def get_part1(data):
    packages = read_input(data)
    in_order_sum = 0
    for i in range(0, len(packages)):
        in_order_sum += i + 1 if is_in_order(*packages[i]) else 0
    return in_order_sum


def get_part2(data):
    pass


result = get_part1("test_data")
assert result == 13, f"got: {result}"

result = get_part1("input_data")
assert result == None, f"got: {result}"

result = get_part2("test_data")
assert result == None, f"got: \n{result}"

result = get_part2("input_data")
assert result == None, f"got: \n{result}"
