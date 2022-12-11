# https://adventofcode.com/2022/day/11

def get_monkeys(data):
    monkeys = []
    with open(data) as f:
        for _ in f:
            monkeys.append({
                'inspection_count': 0,
                'items': [int(item.strip()) for item in next(f)[17:].split(',')],
                'op': next(f)[18:].strip().split(),
                'mod': int(next(f)[21:].strip()),
                'throw_true': int(next(f)[29:].strip()),
                'throw_false': int(next(f)[30:].strip())
            })
            next(f, '')
    return monkeys


def play_keep_away(monkeys, rounds, mod_product=None):
    for _ in range(0, rounds):
        for i in range(0, len(monkeys)):
            monkey = monkeys[i]
            for item in monkey['items']:
                monkey['inspection_count'] += 1
                item = calc_worry_level(item, *monkey['op'], mod_product)
                to_monkey = monkey['throw_true'] if item % monkey['mod'] == 0 else monkey['throw_false']
                monkeys[to_monkey]['items'].append(item)
            monkey['items'] = []
    return monkeys


def calc_worry_level(item, num1, op, num2, mod_product=None):
    num1, num2 = get_num(item, num1), get_num(item, num2)
    worry = num1 * num2 if op == "*" else (num1 + num2)
    if mod_product:
        return worry % mod_product
    else:
        return worry // 3


def calc_worry_level_part2(item, num1, op, num2, mod_product):
    num1, num2 = get_num(item, num1), get_num(item, num2)
    return ((num1 * num2) if op == "*" else (num1 + num2)) % mod_product


def get_num(item, num):
    return item if num == 'old' else int(num)


def get_mods_product(monkeys):
    mod_product = 1
    for monkey in monkeys:
        mod_product *= monkey['mod']
    return mod_product


def get_part1(data):
    monkeys = play_keep_away(get_monkeys(data), 20)
    inspection_counts = [monkey['inspection_count'] for monkey in monkeys]
    print(inspection_counts)
    inspection_counts = sorted(inspection_counts)
    return inspection_counts[-1] * inspection_counts[-2]


def get_part2(data):
    monkeys = get_monkeys(data)
    monkeys = play_keep_away(monkeys, 10000, get_mods_product(monkeys))
    inspection_counts = [monkey['inspection_count'] for monkey in monkeys]
    print(inspection_counts)
    inspection_counts = sorted(inspection_counts)
    return inspection_counts[-1] * inspection_counts[-2]


result = get_part1("test_data")
assert result == 10605, f"got: {result}"
result = get_part1("input_data")
assert result == 55930, f"got: {result}"

result = get_part2("test_data")
assert result == 2713310158, f"got: \n{result}"
result = get_part2("input_data")
assert result == 14636993466, f"got: \n{result}"
