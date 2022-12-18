# https://adventofcode.com/2022/day/17
import random

HEIGHT_ADDED = 4


def tetris(jets_sequence, rock_count):
    counter = 0
    current_max_height = 0
    rock_patterns = [
        [(2, 0), (3, 0), (4, 0), (5, 0)],  # -
        [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],  # +
        [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],  # _|
        [(2, 0), (2, 1), (2, 2), (2, 3)],  # |
        [(2, 0), (3, 0), (2, 1), (3, 1)],  # #
    ]
    matrix = {
        (0, 0): "_",
        (1, 0): "_",
        (2, 0): "_",
        (3, 0): "_",
        (4, 0): "_",
        (5, 0): "_",
        (6, 0): "_"
    }
    while counter < rock_count:
        shape_last_height = 0
        shape = move_shape(next_value(rock_patterns), 0, current_max_height + HEIGHT_ADDED)
        shape_height = get_max_height(shape)
        counter += 1
        print(f'rock #{counter}')
        while shape_height is not shape_last_height:
            # print_matrix(matrix, current_max_height + HEIGHT_ADDED, shape)
            jet_push = next_value(jets_sequence)
            shape = move_shape(shape, jet_push, 0) if is_valid_move(matrix, shape, jet_push, 0) else shape
            shape_last_height = get_max_height(shape)
            shape = move_shape(shape, 0, -1) if is_valid_move(matrix, shape, 0, - 1) else shape
            shape_height = get_max_height(shape)
        # print_matrix(matrix, current_max_height + HEIGHT_ADDED, shape, 30)
        current_max_height = max(current_max_height, shape_height)
        letter = chr(random.randint(65, 90))
        for loc in shape:
            matrix[loc] = letter

    print_matrix(matrix, current_max_height + HEIGHT_ADDED, shape, 30)
    return current_max_height


def next_value(l):
    value = l.pop(0)
    l.append(value)
    return value


def get_max_height(shape):
    return max(y for _, y in shape)


def move_shape(shape, x, y):
    return [tuple(map(sum, zip(coord, (x, y)))) for coord in shape]


def is_valid_move(matrix, shape, m_x, m_y):
    for s_x, s_y in shape:
        x = s_x + m_x
        y = s_y + m_y
        if x < 0 or x > 6:
            return False
        if (x, y) in matrix:
            return False
    return True


def print_matrix(matrix, max_height, shape=[], max=0):
    max = max_height - max if max is not 0 and max < max_height else 0
    for y in range(max_height, -1 + max, -1):
        print("|", end="")
        for x in range(0, 7):
            value = matrix[(x, y)] if (x, y) in matrix else "@" if (x, y) in shape else "."
            print(value, end="")
        print("|")
    if max > 0:
        print(f'last {max} rows not shows...')


def get_part1(data):
    jets_sequence = [1 if c == ">" else -1 for c in open(data).read()]
    return tetris(jets_sequence, 2022)


def get_part2(data):
    jets_sequence = [1 if c == ">" else -1 for c in open(data).read()]
    return tetris(jets_sequence, 1000000000000)


result = get_part1("test_data")
assert result == 3068, f"got: {result}"
result = get_part1("input_data")
assert result == 3098, f"got: {result}"

result = get_part2("test_data")
assert result == 1514285714288, f"got: \n{result}"

result = get_part2("input_data")
assert result == 1, f"got: \n{result}"
