# https://adventofcode.com/2022/day/2

def calc_strategy_score_part1(input_file):
    plays = ["X", "Y", "Z"]
    final_score = 0
    with open(input_file) as f:
        for line in f.read().splitlines():
            outcome_score = 6 if line in ["A Y", "B Z", "C X"] else 3 if line in ["A X", "B Y", "C Z"] else 0
            shape_score = plays.index(line.split(" ")[1]) + 1
            final_score += outcome_score + shape_score
    return final_score


def calc_strategy_score_part2(input_file):
    hands = ["A", "B", "C"]
    outcomes = ["X", "Y", "Z"]
    final_score = 0
    with open(input_file) as f:
        for line in f.read().splitlines():
            hand, outcome = line.split(" ")
            outcome_ndx = outcomes.index(outcome)
            hand_score = (hands.index(hand) + outcome_ndx - 1) % 3 + 1
            outcome_score = outcome_ndx * 3
            final_score += hand_score + outcome_score
            # print(f'{line} - {hand_score} + {outcome_score}')
    return final_score


assert calc_strategy_score_part1('test_data') == 15

print(f'answer: {calc_strategy_score_part1("input_data")}')

assert calc_strategy_score_part2('test_data') == 12

print(f'answer: {calc_strategy_score_part2("input_data")}')
