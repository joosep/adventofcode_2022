# https://adventofcode.com/2022/day/8

def get_part1(data):
    tree_visibility_matrix = fill_matrix(data, row_tree_visibility)
    return sum(i for row in tree_visibility_matrix for i in row)


def row_tree_visibility(row, result_row):
    max_height = -1
    for i in range(0, len(row)):
        height = int(row[i])
        if height > max_height:
            result_row[i], max_height = 1, height
    return result_row


def get_part2(data):
    trees_seen_matrix = fill_matrix(data, row_trees_seen, 1)
    return max(i for row in trees_seen_matrix for i in row)


def row_trees_seen(row, result_row):
    for tree_ndx in range(0, len(row)):
        seen = 0
        for j in range(tree_ndx + 1, len(row)):
            seen += 1
            if row[tree_ndx] <= row[j]:
                break
        result_row[tree_ndx] *= seen
    return result_row


def fill_matrix(data, fun, default_value=0):
    content = open(data).read().splitlines()
    print_matrix(content)
    result_matrix = fill_matrix_per_row(content, [[default_value for _ in row] for row in content], fun)
    result_matrix = transpose(fill_matrix_per_row(transpose(content), transpose(result_matrix), fun))
    print_matrix(result_matrix)
    return result_matrix


def fill_matrix_per_row(data, result_matrix, fun):
    return [fill_row(row, result_row, fun) for (row, result_row) in list(zip(data, result_matrix))]


def fill_row(row, result_row, fun):
    result_row = fun(row, result_row)
    result_row = reverse(fun(reverse(row), reverse(result_row)))
    return result_row


def print_matrix(m):
    for r in m:
        print(r)


def transpose(m):
    return list(map(list, zip(*m)))


def reverse(r):
    return r[::-1]


assert get_part1("test_data") == 21
assert get_part1("input_data") == 1809

assert get_part2("test_data") == 8
assert get_part2("input_data") == 479400
