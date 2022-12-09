# https://adventofcode.com/2022/day/9

X, Y, HEAD = 0, 1, 0


def find_tail_positions_count(data, knots_count):
    knots = [[0, 0] for _ in range(0, knots_count)]
    tail_positions = set()
    for direction, count in map(lambda line: line.split(), open(data).read().splitlines()):
        move_knots(direction, int(count), knots, tail_positions)
    print_movements(knots, tail_positions)
    return len(tail_positions)


def move_knots(direction, count, knots, tail_positions):
    for i in range(0, count):
        if direction == "R":
            knots[HEAD][X] += 1
        elif direction == "L":
            knots[HEAD][X] -= 1
        elif direction == "U":
            knots[HEAD][Y] += 1
        elif direction == "D":
            knots[HEAD][Y] -= 1
        for tail_ndx in range(1, len(knots)):
            move_knot(knots, tail_ndx)
            collect_tail_position(knots, tail_positions)


def move_knot(knots, knot_ndx):
    head_knot = knots[knot_ndx - 1]
    move_x, move_y = 0, 0
    dist_x = head_knot[X] - knots[knot_ndx][X]
    dist_y = head_knot[Y] - knots[knot_ndx][Y]
    if abs(dist_x) > 1 and abs(dist_y) > 1:
        move_x = dist_x // 2
        move_y = dist_y // 2
    elif abs(dist_x) > 1:
        move_x = dist_x // 2
        move_y = dist_y
    elif abs(dist_y) > 1:
        move_x = dist_x
        move_y = dist_y // 2
    knots[knot_ndx][X] += move_x
    knots[knot_ndx][Y] += move_y


def collect_tail_position(knots, tail_positions):
    knot = knots[len(knots) - 1]
    return tail_positions.add(f'{knot[X]} {knot[Y]}')


def print_movements(knots, tail_positions):
    min_x = min(int(pos) for pos in map(lambda a: a.split()[X], tail_positions))
    min_x = min(min_x, min(pos[X] for pos in knots))
    min_y = min(int(pos) for pos in map(lambda a: a.split()[Y], tail_positions))
    min_y = min(min_y, min(pos[Y] for pos in knots))
    max_x = max(int(pos) for pos in map(lambda a: a.split()[X], tail_positions))
    max_x = max(max_x, max(pos[X] for pos in knots))
    max_y = max(int(pos) for pos in map(lambda a: a.split()[Y], tail_positions))
    max_y = max(max_y, max(pos[Y] for pos in knots))
    print()
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            value = [x, y]
            if value in knots:
                num = knots.index(value)
                print(num, end=' ')
            elif f'{x} {y}' in tail_positions:
                print('#', end=' ')
            elif x == y == 0:
                print('S', end=' ')
            else:
                print('.', end=' ')
        print()


def get_part1(data):
    return find_tail_positions_count(data, 2)


def get_part2(data):
    return find_tail_positions_count(data, 10)


assert get_part1("test_data") == 13
assert get_part1("input_data") == 6314
assert get_part2("test_data") == 1
assert get_part2("test_data_part2") == 36
assert get_part2("input_data") == 2504
