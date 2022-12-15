# https://adventofcode.com/2022/day/15


def get_number_of_non_beacons(data, y_axis):
    empty_x_values = set()
    beacon_x_values = set()
    for line in [line.replace(",", "").replace(":", "").split() for line in open(data).read().splitlines()]:
        s_x, s_y = get_num(line[2]), get_num(line[3])
        b_x, b_y = get_num(line[8]), get_num(line[9])
        distance_diff = abs(s_x - b_x) + abs(s_y - b_y) - abs(s_y - y_axis)
        for x in range(s_x - distance_diff, s_x + distance_diff + 1):
            empty_x_values.add(x)
        if b_y == y_axis:
            beacon_x_values.add(b_x)
    return len(empty_x_values - beacon_x_values)


def get_missing_beacon(data, max_distance):
    sensor_x_y_distance = []
    for line in [line.replace(",", "").replace(":", "").split() for line in open(data).read().splitlines()]:
        s_x, s_y = get_num(line[2]), get_num(line[3])
        b_x, b_y = get_num(line[8]), get_num(line[9])
        sensor_x_y_distance.append((s_x, s_y, abs(s_x - b_x) + abs(s_y - b_y)))
    sensor_x_y_distance = sorted(sensor_x_y_distance)  # sort by x
    for y in range(0, max_distance + 1):
        x = 0
        for s_x, s_y, s_d in sensor_x_y_distance:
            distance_left_for_x = s_d - abs(s_y - y)
            x_diff = abs(x - s_x)
            if distance_left_for_x >= x_diff:
                x = s_x + distance_left_for_x
        if x < max_distance:
            return x + 1, y


def get_tuning_frequence(data, max_distance):
    x, y = get_missing_beacon(data, max_distance)
    return x * 4000000 + y


def get_num(string):
    return int(string.split('=')[1])


def print_matrix(data, max_range=None):
    matrix = {}
    max_x, min_x, max_y, min_y = 0, 2 ** 63 - 1, 0, 2 ** 63 - 1
    for line in [line.replace(",", "").replace(":", "").split() for line in open(data).read().splitlines()]:
        sensor = get_num(line[2]), get_num(line[3])
        beacon = get_num(line[8]), get_num(line[9])
        matrix[sensor] = "S"
        matrix[beacon] = "B"
        min_x, max_x = min(min_x, beacon[0], sensor[0]), max(max_x, beacon[0], sensor[0]),
        min_y, max_y = min(min_y, beacon[1], sensor[1]), max(max_y, beacon[1], sensor[1])
        distance = get_distance(sensor, beacon)
        for x in range(sensor[0] - distance, sensor[0] + distance + 1):
            for y in range(sensor[1] - distance, sensor[1] + distance):
                empty = x, y
                if get_distance(sensor, empty) <= distance:
                    matrix[empty] = "#" if empty not in matrix else matrix[empty]
                    min_x, max_x = min(min_x, x), max(max_x, x)
                    min_y, max_y = min(min_y, y), max(max_y, y)
    if max_range:
        max_x, min_x, max_y, min_y = max_range, 0, max_range, 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            value = matrix[(x, y)] if (x, y) in matrix else "."
            print(value, end='')
        print()
    print()


def get_distance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def get_part1(data, y_coord):
    return get_number_of_non_beacons(data, y_coord)


def get_part2(data, max_distance):
    return get_tuning_frequence(data, max_distance)


print_matrix("test_data")
print_matrix("test_data", 20)

result = get_part1("test_data", 10)
assert result == 26, f"got: {result}"

result = get_part1("input_data", 2000000)
assert result == 5461729, f"got: {result}"

result = get_part2("test_data", 20)
assert result == 56000011, f"got: \n{result}"

result = get_part2("input_data", 4000000)
assert result == 10621647166538, f"got: \n{result}"
