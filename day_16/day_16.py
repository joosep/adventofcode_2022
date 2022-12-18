# https://adventofcode.com/2022/day/16

def read_valves(data):
    valves = {}
    for line in [line.replace(";", "").replace(", ", "-").split() for line in open(data).read().splitlines()]:
        valves[line[1]] = {
            "rate": int(line[4].split("=")[1]),
            "valves": line[9].split("-")
        }
    for v1 in valves:
        valves[v1]["valves"].sort(key=lambda x: valves[x]["rate"])
        valves[v1]["distances"] = {}
        for v2 in valves:
            if not v1 == v2:
                valves[v1]["distances"][v2] = find_shortest_path(v1, v2, valves)
    return valves


def find_shortest_path(v_s, v_e, valves):
    visited = [v_s]
    traj_length = [(v_s, 0)]
    while traj_length:
        v_c, count = traj_length.pop(0)
        if v_c == v_e:
            return count
        for v_n in valves[v_c]["valves"]:
            if v_n not in visited:
                traj_length.append((v_n, count + 1))
                visited.append(v_n)


def walk(valve, valves, time):
    opened_valves = set([valve for valve in valves if valves[valve]['rate'] == 0])
    max_released_pressure, released = 0, 0
    valves_to_check = [(valve, time, released, opened_valves)]
    while valves_to_check:
        valve, time, released, opened_valves = valves_to_check.pop(0)
        if time <= 1:
            old_max = max_released_pressure
            max_released_pressure = max(max_released_pressure, released)
            if old_max != max_released_pressure:
                print(max_released_pressure)
            continue
        possible_future_max = get_future_max(valves, valve, time, opened_valves)
        if released + possible_future_max < max_released_pressure:
            continue
        time -= 1  # move or open
        for valve_new in valves[valve]['valves']:
            valves_to_check.insert(0, (valve_new, time, released, opened_valves))
        if valve not in opened_valves:
            released_new = released + valves[valve]['rate'] * time
            time_new = time - 1  # move
            valved_opened_new = opened_valves.copy()
            valved_opened_new.add(valve)
            for valve_new in valves[valve]['valves']:
                valves_to_check.insert(0, (valve_new, time_new, released_new, valved_opened_new))
    return max_released_pressure


def get_future_max(valves, valve, time, opened_valves):
    future_sum = (time - 1) * valves[valve]["rate"] if valve not in opened_valves else 0
    distance_v = [v for v in valves[valve]["distances"] if v not in opened_valves]
    for v in distance_v:
        future_sum += max(0, (time - valves[valve]["distances"][v] - 1) * valves[v]["rate"])
    return future_sum


def walk_tandem(v_locs, valves, time):
    opened_valves = set([valve for valve in valves if valves[valve]['rate'] == 0])
    max_released_pressure, released = 0, 0
    released = 0
    valves_to_check = [(v_locs, time, released, opened_valves)]
    while valves_to_check:
        v_locs, time, released, opened_valves = valves_to_check.pop(0)
        if time <= 1:
            old_max = max_released_pressure
            max_released_pressure = max(max_released_pressure, released)
            if old_max != max_released_pressure:
                print(max_released_pressure)
            continue
        possible_future_max = get_future_max(valves, v_locs, time, opened_valves)
        if released + possible_future_max < max_released_pressure:
            continue
        time -= 1  # move or open
        for valve_new in valves[v_locs]['valves']:
            valves_to_check.insert(0, (valve_new, time, released, opened_valves))
        if v_locs not in opened_valves:
            released_new = released + valves[v_locs]['rate'] * time
            time_new = time - 1  # move
            valved_opened_new = opened_valves.copy()
            valved_opened_new.add(v_locs)
            for valve_new in valves[v_locs]['valves']:
                valves_to_check.insert(0, (valve_new, time_new, released_new, valved_opened_new))
    return max_released_pressure


def get_part1(data):
    valves = read_valves(data)
    return walk("AA", valves, 30)


def get_part2(data):
    valves = read_valves(data)
    return walk_tandem(("AA", "AA"), valves, 26)


result = get_part1("test_data")
assert result == 1651, f"got: {result}"
# result = get_part1("input_data")
# assert result == 2330, f"got: {result}"

result = get_part2("test_data")
assert result == 1707, f"got: \n{result}"

result = get_part2("input_data")
assert result == 10621647166538, f"got: \n{result}"
