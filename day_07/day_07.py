# https://adventofcode.com/2022/day/7


def calc_dir_sizes(f, path=None):
    directories = {}
    size = 0
    for line in f:
        parts = line.strip().split(" ")
        if parts[0] == "$" and parts[1] == "cd":
            dir_name = parts[2]
            if dir_name == "..":
                directories[path] = size
                return directories, size
            subdirectories, dir_size = calc_dir_sizes(f, path + dir_name + "/" if path else dir_name)
            directories |= subdirectories
            size += dir_size
        elif parts[0].isnumeric():
            size += int(parts[0])
        if path:
            directories[path] = size
    return directories, size


def get_part1(data):
    directories, _ = calc_dir_sizes(open(data))
    print(directories)
    return sum(v for v in directories.values() if v <= 100000)


def get_part2(data):
    directories, size = calc_dir_sizes(open(data))
    need_to_delete = 30000000 - (70000000 - size)
    print(f'need to delete: {need_to_delete}')
    print(directories)
    return min(v for v in directories.values() if v >= need_to_delete)


assert get_part1("test_data") == 95437
assert get_part1("input_data") == 1517599

assert get_part2("test_data") == 24933642
assert get_part2("input_data") == 2481982
