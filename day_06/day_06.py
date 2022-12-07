# https://adventofcode.com/2022/day/6

def get_match_index(l, length=4):
    for i in range(0, len(l)):
        marker = set(l[i + j] for j in range(0, length))
        if len(marker) == length:
            return i + length


# part 1
assert get_match_index('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert get_match_index('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert get_match_index('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert get_match_index('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

print(f'answer: {get_match_index(open("input_data").readline())}')

# part 2
assert get_match_index('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
assert get_match_index('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
assert get_match_index('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
assert get_match_index('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
assert get_match_index('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26

print(f'answer: {get_match_index(open("input_data").readline(), 14)}')
