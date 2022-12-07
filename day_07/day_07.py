# https://adventofcode.com/2022/day/7


def calc_dir_size(f, path, directories):
    size = 0
    for line in f:
        parts = line.strip().split(" ")
        if parts[0] == "$" and parts[1] == "cd":
            dir_name = parts[2]
            if dir_name == "..":
                directories[path] = size
                return size
            dir_size = calc_dir_size(f, path + dir_name + "/", directories)
            size += dir_size
        elif parts[0].isnumeric():
            size += int(parts[0])
    if path != "":
        directories[path] = size
    return size


def get_part1(data):
    directories = {}
    calc_dir_size(open(data), "", directories)
    print(directories)
    return sum(v if v <= 100000 else 0 for v in directories.values())


def get_part2(data):
    directories = {}
    calc_dir_size(open(data), "", directories)
    need_to_delete = 30000000 - (70000000 - directories["//"])
    print(f'need to delete: {need_to_delete}')
    print(directories)
    return min(v if v >= need_to_delete else 70000000 for v in directories.values())


assert get_part1("test_data") == 95437
print(f'answer: {get_part1("input_data")}')

assert get_part2("test_data") == 24933642
print(f'answer: {get_part2("input_data")}')
