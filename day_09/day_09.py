# https://adventofcode.com/2022/day/9

X, Y, HEAD = 0, 1, 0

MOVES = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}


def find_tail_positions_count(data, knots_count):
    knots, tail_positions = [[0, 0] for _ in range(0, knots_count)], set()
    for direction, count in map(lambda line: line.split(), open(data).read().splitlines()):
        move_knots(MOVES[direction], int(count), knots, tail_positions)
    print_movements(knots, tail_positions)
    return len(tail_positions)


def move_knots(move, count, knots, tail_positions):
    for i in range(0, count):
        knots[HEAD] = apply_move(knots[HEAD], move)
        for tail_ndx in range(1, len(knots)):
            move_knot(knots, tail_ndx)
            collect_tail_position(knots, tail_positions)


def move_knot(knots, knot_ndx):
    head_knot, knot, move = knots[knot_ndx - 1], knots[knot_ndx], [0, 0]
    dist = [head_knot[X] - knot[X], head_knot[Y] - knot[Y]]
    if abs(dist[X]) > 1 and abs(dist[Y]) > 1:
        move = [dist[X] // 2, dist[Y] // 2]
    elif abs(dist[X]) > 1:
        move = [dist[X] // 2, dist[Y]]
    elif abs(dist[Y]) > 1:
        move = [dist[X], dist[Y] // 2]
    knots[knot_ndx] = apply_move(knot, move)


def apply_move(knot, move):
    return [knot[X] + move[X], knot[Y] + move[Y]]


def collect_tail_position(knots, tail_positions):
    knot = knots[len(knots) - 1]
    return tail_positions.add(f'{knot[X]} {knot[Y]}')


def print_movements(knots, tail_positions):
    min_x = min(min(int(pos) for pos in map(lambda a: a.split()[X], tail_positions)), min(pos[X] for pos in knots))
    min_y = min(min(int(pos) for pos in map(lambda a: a.split()[Y], tail_positions)), min(pos[Y] for pos in knots))
    max_x = max(max(int(pos) for pos in map(lambda a: a.split()[X], tail_positions)), max(pos[X] for pos in knots))
    max_y = max(max(int(pos) for pos in map(lambda a: a.split()[Y], tail_positions)), max(pos[Y] for pos in knots))
    print()
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if [x, y] in knots:
                print(knots.index([x, y]), end=' ')
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
