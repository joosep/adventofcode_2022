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
        length = max((max_x - min_x) // 2, max_y + 2)
        max_x, min_x, max_y = 500 + length, 500 - length, max_y + 2
        for i in range(min_x, max_x + 1):
            matrix[(i, max_y)] = "#"
    return matrix, (min_x, min_y), (max_x, max_y)


def print_matrix(matrix, min_coord, max_coord):
    for y in range(min_coord[1], max_coord[1] + 1):
        for x in range(min_coord[0], max_coord[0] + 1):
            value = matrix[(x, y)] if (x, y) in matrix else "."
            print(value, end='')
        print()
    print()


def fill_with_sand(matrix, min_coord, max_coord):
    starting_coord = 500, 0
    sand_coords = starting_coord
    sand_counter = 0
    while True:
        new_sand_coords = move_sand(matrix, *sand_coords)
        if not min_coord[0] <= new_sand_coords[0] <= max_coord[0] or \
                not min_coord[1] <= new_sand_coords[1] <= max_coord[1]:
            return sand_counter
        if sand_coords == new_sand_coords:
            sand_counter += 1
            matrix[new_sand_coords] = "o"
            if new_sand_coords == starting_coord:
                return sand_counter
            sand_coords = starting_coord
        else:
            sand_coords = new_sand_coords


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
    matrix, min_coord, max_coord = read_data(data)
    print_matrix(matrix, min_coord, max_coord)
    counter = fill_with_sand(matrix, min_coord, max_coord)
    print_matrix(matrix, min_coord, max_coord)
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
