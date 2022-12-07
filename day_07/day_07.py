# https://adventofcode.com/2022/day/7


def calc_dir_size(f, dir_path=None):
    dirs, dir_size = {}, 0
    for line in f:
        parts = line.strip().split(" ")
        if parts[0] == "$" and parts[1] == "cd":
            dir_name = parts[2]
            if dir_name == "..":
                dirs[dir_path] = dir_size
                return dirs, dir_size
            subdirs, subdirs_size = calc_dir_size(f, dir_path + dir_name + "/" if dir_path else dir_name)
            dirs |= subdirs
            dir_size += subdirs_size
        elif parts[0].isnumeric():
            dir_size += int(parts[0])
        if dir_path:
            dirs[dir_path] = dir_size
    return dirs, dir_size


def get_part1(data):
    dirs, _ = calc_dir_size(open(data))
    print(dirs)
    return sum(v for v in dirs.values() if v <= 100000)


def get_part2(data):
    dirs, size = calc_dir_size(open(data))
    need_to_delete = 30000000 - (70000000 - size)
    print(f'need to delete: {need_to_delete}')
    print(dirs)
    return min(v for v in dirs.values() if v >= need_to_delete)


assert get_part1("test_data") == 95437
assert get_part1("input_data") == 1517599

assert get_part2("test_data") == 24933642
assert get_part2("input_data") == 2481982
