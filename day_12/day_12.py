# https://adventofcode.com/2022/day/12

START = ord('S')
END = ord('E')


def find_shortest_path(data, move_uphill=True):
    matrix = read_input(data)
    starting_coords = find_starting_coords(matrix, START if move_uphill else END)
    end_value = END if move_uphill else ord('a')
    visited = [starting_coords]
    traj_length = [(starting_coords, 0)]
    while traj_length:
        current_coords, count = traj_length.pop(0)
        if get_value(matrix, current_coords) == end_value:
            return count
        for adjacent in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_coords = tuple(map(sum, zip(current_coords, adjacent)))
            if is_inside_borders(matrix, new_coords) \
                    and new_coords not in visited \
                    and is_height_ok(matrix, current_coords, new_coords, move_uphill):
                traj_length.append((new_coords, count + 1))
                visited.append(new_coords)


def read_input(data):
    return [[ord(c) for c in row] for row in open(data).read().splitlines()]


def find_starting_coords(matrix, starting_value):
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            if matrix[x][y] == starting_value:
                return x, y


def get_value(matrix, coords):
    return matrix[coords[0]][coords[1]]


def is_inside_borders(matrix, coords):
    return 0 <= coords[0] < len(matrix) and 0 <= coords[1] < len(matrix[coords[0]])


def is_height_ok(matrix, current_coords, new_coords, move_uphill):
    current_height = fix_s_and_e_values(get_value(matrix, current_coords))
    new_height = fix_s_and_e_values(get_value(matrix, new_coords))
    return new_height - current_height <= 1 if move_uphill else current_height - new_height <= 1


def fix_s_and_e_values(height):
    return ord('a') if height == START else ord('z') if height == END else height


def get_part1(data):
    return find_shortest_path(data)


def get_part2(data):
    return find_shortest_path(data, move_uphill=False)


result = get_part1("test_data")
assert result == 31, f"got: {result}"

result = get_part1("input_data")
assert result == 517, f"got: {result}"
result = get_part2("test_data")
assert result == 29, f"got: \n{result}"
result = get_part2("input_data")
assert result == 512, f"got: \n{result}"
