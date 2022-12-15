# https://adventofcode.com/2022/day/14

def read_data(data, has_bottom=False):
    matrix = {}
    max_x, min_x, max_y, min_y = 0, 2 ** 63 - 1, 0, 0
    for line in open(data).read().splitlines():
        last_x, last_y = None, None
        line = line.replace("-", "").replace(" ", "")
        for x, y in [map(int, coords.split(',')) for coords in line.split(">")]:
            max_x, max_y, min_x, min_y = max(max_x, x), max(max_y, y), min(min_x, x), min(min_y, y)
            if last_x is not None:
                for cur_x in range(min(last_x, x), max(last_x, x) + 1):
                    for cur_y in range(min(last_y, y), max(last_y, y) + 1):
                        matrix[(cur_x, cur_y)] = "#"
            last_x, last_y = x, y
    if has_bottom:
        bottom_length = max((max_x - min_x) // 2, max_y + 2)
        max_x, min_x, max_y = 500 + bottom_length, 500 - bottom_length, max_y + 2
        for i in range(min_x, max_x + 1):
            matrix[(i, max_y)] = "#"
    return matrix, (min_x, min_y), (max_x, max_y)


def print_matrix(matrix, min_loc, max_loc):
    for y in range(min_loc[1], max_loc[1] + 1):
        for x in range(min_loc[0], max_loc[0] + 1):
            value = matrix[(x, y)] if (x, y) in matrix else "."
            print(value, end='')
        print()
    print()


def fill_with_sand(matrix, min_loc, max_loc):
    starting_loc = 500, 0
    sand_loc = starting_loc
    sand_counter = 0
    while True:
        new_sand_loc = move_sand(matrix, *sand_loc)
        if not min_loc[0] <= new_sand_loc[0] <= max_loc[0] or \
                not min_loc[1] <= new_sand_loc[1] <= max_loc[1]:
            return sand_counter
        if sand_loc == new_sand_loc:
            sand_counter += 1
            matrix[new_sand_loc] = "o"
            if new_sand_loc == starting_loc:
                return sand_counter
            sand_loc = starting_loc
        else:
            sand_loc = new_sand_loc


def move_sand(matrix, x, y):
    one_down = x, y + 1
    if one_down not in matrix:
        return one_down
    else:
        one_down_and_left = x - 1, y + 1
        if one_down_and_left not in matrix:
            return one_down_and_left
        else:
            one_down_and_right = x + 1, y + 1
            if one_down_and_right not in matrix:
                return one_down_and_right
            else:
                return x, y


def get_part1(data):
    matrix, min_loc, max_loc = read_data(data)
    print_matrix(matrix, min_loc, max_loc)
    counter = fill_with_sand(matrix, min_loc, max_loc)
    print_matrix(matrix, min_loc, max_loc)
    return counter


def get_part2(data):
    matrix, min_coord, max_coord = read_data(data, has_bottom=True)
    print_matrix(matrix, min_coord, max_coord)
    counter = fill_with_sand(matrix, min_coord, max_coord)
    print_matrix(matrix, min_coord, max_coord)
    return counter


result = get_part1("test_data")
assert result == 24, f"got: {result}"

result = get_part1("input_data")
assert result == 961, f"got: {result}"

result = get_part2("test_data")
assert result == 93, f"got: \n{result}"

result = get_part2("input_data")
assert result == 26375, f"got: \n{result}"
