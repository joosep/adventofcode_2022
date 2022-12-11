# https://adventofcode.com/2022/day/11

def get_monkeys(data):
    monkeys = []
    with open(data) as f:
        for _ in f:
            monkeys.append({
                'inspection_count': 0,
                'items': [int(item.strip()) for item in next(f)[17:].split(',')],
                'op': next(f)[18:].strip().split(),
                'test': int(next(f)[21:].strip()),
                'throw_true': int(next(f)[29:].strip()),
                'throw_false': int(next(f)[30:].strip())
            })
            next(f, '')
    return monkeys


def play_keep_away(monkeys, rounds):
    for _ in range(0, rounds):
        for i in range(0, len(monkeys)):
            monkey = monkeys[i]
            for _ in range(0, len(monkey['items'])):
                item = monkey['items'].pop(0)
                monkey['inspection_count'] += 1
                item = calc_worry_level(item, *monkey['op'])
                to_monkey = monkey['throw_true'] if item % monkey['test'] == 0 else monkey['throw_false']
                monkeys[to_monkey]['items'].append(item)
    return monkeys


def calc_worry_level(item, num1, op, num2):
    num1 = item if num1 == 'old' else int(num1)
    num2 = item if num2 == 'old' else int(num2)
    return (num1 * num2) // 3 if op == "*" else (num1 + num2) // 3


def get_part1(data):
    monkeys = play_keep_away(get_monkeys(data), 20)
    inspection_counts = [monkey['inspection_count'] for monkey in monkeys]
    inspection_counts = sorted(inspection_counts)
    print(inspection_counts)
    return inspection_counts[-1] * inspection_counts[-2]


def get_part2(data):
    monkeys = play_keep_away(get_monkeys(data), 10000)
    inspection_counts = [monkey['inspection_count'] for monkey in monkeys]
    print(inspection_counts)
    inspection_counts = sorted(inspection_counts)
    print(inspection_counts)
    return inspection_counts[-1] * inspection_counts[-2]


result = get_part1("test_data")
assert result == 10605, f"got: {result}"
result = get_part1("input_data")
assert result == 55930, f"got: {result}"
exit()
result = get_part2("test_data")
assert result == 2713310158, f"got: \n{result}"

result = get_part2("input_data")
assert get_part2("input_data") == None, f"got: \n{result}"
