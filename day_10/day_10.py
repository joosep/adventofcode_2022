# https://adventofcode.com/2022/day/10

def get_register_values(data):
    x = 1
    register_value = []
    for args in map(lambda a: a.split(), open(data).read().splitlines()):
        if args[0] == "noop":
            register_value.append(x)
        elif args[0] == "addx":
            for _ in range(0, 2):
                register_value.append(x)
            x += int(args[1])
    return register_value


def get_register_values_simplified(data):
    x = 1
    register_value = []
    for args in map(lambda a: a.split(), open(data).read().splitlines()):
        register_value.append(x)
        if args[0] == "addx":
            register_value.append(x)
            x += int(args[1])
    return register_value


def print_image(register_values):
    image = ""
    for i in range(0, len(register_values)):
        sprite_loc = register_values[i] - 1
        if 0 <= (i % 40) - sprite_loc < 3:
            image += "#"
        else:
            image += "."
        if (i + 1) % 40 == 0:
            image += "\n"
    return image


def get_part1(data):
    register_values = get_register_values_simplified(data)
    return sum(cycle * register_values[cycle - 1] for cycle in range(20, 221, 40))


def get_part2(data):
    register_values = get_register_values_simplified(data)
    return print_image(register_values)


result = get_part1("test_data")
assert result == 13140, f"got: {result}"
result = get_part1("input_data")
assert result == 11780, f"got: {result}"

expected = "##..##..##..##..##..##..##..##..##..##..\n" \
           "###...###...###...###...###...###...###.\n" \
           "####....####....####....####....####....\n" \
           "#####.....#####.....#####.....#####.....\n" \
           "######......######......######......####\n" \
           "#######.......#######.......#######.....\n"
result = get_part2("test_data")
assert result == expected, f"got: \n{result}"

result = get_part2("input_data")
expected = "###..####.#..#.#....###...##..#..#..##..\n" \
           "#..#....#.#..#.#....#..#.#..#.#..#.#..#.\n" \
           "#..#...#..#..#.#....###..#..#.#..#.#..#.\n" \
           "###...#...#..#.#....#..#.####.#..#.####.\n" \
           "#....#....#..#.#....#..#.#..#.#..#.#..#.\n" \
           "#....####..##..####.###..#..#..##..#..#.\n"
assert get_part2("input_data") == expected, f"got: \n{result}"
