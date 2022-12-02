# https://adventofcode.com/2022/day/1
def create_calories_list(input_file):
    with open(input_file) as f:
        calories = [sum(int(c) if c != "" else 0 for c in calories.split('\n')) for calories in f.read().split('\n\n')]
        return sorted(calories, reverse=True)


def find_most_calories(input_file):
    return create_calories_list(input_file)[0]


def find_most_3_calories(input_file):
    return sum(create_calories_list(input_file)[0:3])


assert find_most_calories('test_data') == 24000

print(f'answer: {find_most_calories("input_data")}')

assert find_most_3_calories('test_data') == 45000

print(f'answer: {find_most_3_calories("input_data")}')
