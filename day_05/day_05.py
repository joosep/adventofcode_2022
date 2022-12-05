# https://adventofcode.com/2022/day/5


def create_stacks(stack_lines):
    reversed_stack = reversed(stack_lines)
    stacks_count = len(next(reversed_stack).split('   '))
    print(stacks_count)
    stacks = {}
    for i in range(0, stacks_count):
        stacks[i + 1] = []
    for row in reversed_stack:
        crates = [row[i + 1:i + 2] for i in range(0, len(row), 4)]
        for i in range(0, len(crates)):
            if crates[i].strip():
                stacks[i + 1].append(crates[i])
    print(stacks)
    return stacks


def calc_part1(input_file):
    with open(input_file) as f:
        stack_lines, movements_lines = [parts.split("\n") for parts in f.read().split("\n\n")]
        stacks = create_stacks(stack_lines)
        for movements in movements_lines:
            if movements:
                _, count, _, from_stack, _, to_stack = movements.split(' ')
                for i in range(0, int(count)):
                    stacks[int(to_stack)].append(stacks[int(from_stack)].pop())
        print(stacks)
        return ''.join([stacks[i].pop() for i in stacks])


def calc_part2(input_file):
    with open(input_file) as f:
        stack_lines, movements_lines = [parts.split("\n") for parts in f.read().split("\n\n")]
        stacks = create_stacks(stack_lines)
        for movements in movements_lines:
            if movements:
                _, count, _, from_stack, _, to_stack = movements.split(' ')
                for i in range(int(count), 0, -1):
                    stack = stacks[int(from_stack)]
                    stacks[int(to_stack)].append(stack.pop(len(stack) - i))

        print(stacks)
        return ''.join([stacks[i].pop() for i in stacks])


assert calc_part1('test_data') == "CMZ"

print(f'answer: {calc_part1("input_data")}')

assert calc_part2('test_data') == "MCD"

print(f'answer: {calc_part2("input_data")}')
