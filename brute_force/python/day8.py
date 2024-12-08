import math

inp = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def parse_input(inp):
    ret = []
    for line in inp.split():
        ret.append(list(line))
    return ret

def print_map(antenna_map):
    for line in antenna_map:
        print(str(line))

def find_antenna_locations(antenna_map):
    seen_to_loc = {}
    for i in range(len(antenna_map)):
        for j in range(len(antenna_map[i])):
            if antenna_map[i][j] != '.':
                if antenna_map[i][j] not in seen_to_loc:
                    seen_to_loc[antenna_map[i][j]] = [(i, j)]
                else:
                    seen_to_loc[antenna_map[i][j]].append((i, j))
    return seen_to_loc

def distance(x1, x2, y1, y2):
    return (x2-x1, y2-y1)

def draw_pair(antenna_map, x1, y1, x2, y2):
    dist_x, dist_y = distance(x1, x2, y1, y2)
    if 0 <= x1 - dist_x < len(antenna_map) and 0 <= y1 - dist_y < len(antenna_map[x1 - dist_x]):
        antenna_map[x1 - dist_x][y1 - dist_y] = '#'

def count_antinodes(antenna_map):
    c = 0
    for line in antenna_map:
        for ch in line:
            if ch == '#':
                c += 1
    return c

def draw_pair_harmonic(antenna_map, x1, y1, x2, y2):
    dist_x, dist_y = distance(x1, x2, y1, y2)
    curr_x, curr_y = x1, y1
    while 0 <= curr_x - dist_x < len(antenna_map) and 0 <= curr_y - dist_y < len(antenna_map[curr_x - dist_x]):
        antenna_map[curr_x - dist_x][curr_y - dist_y] = '#'
        curr_x, curr_y = curr_x - dist_x, curr_y - dist_y
    curr_x, curr_y = x1, y1
    while 0 <= curr_x + dist_x < len(antenna_map) and 0 <= curr_y + dist_y < len(antenna_map[curr_x + dist_x]):
        antenna_map[curr_x + dist_x][curr_y + dist_y] = '#'
        curr_x, curr_y = curr_x + dist_x, curr_y + dist_y

def part1(antenna_map, type_to_loc):
    type_to_loc = find_antenna_locations(antenna_map)
    # print(type_to_loc)
    for antenna_type, locations in type_to_loc.items():
        for i in range(len(locations)):
            for j in range(len(locations)):
                if i != j:
                    draw_pair(antenna_map, locations[i][0], locations[i][1], locations[j][0], locations[j][1])
    # print_map(antenna_map)
    ctr = count_antinodes(antenna_map)
    print(ctr)

def part2(antenna_map, type_to_loc):
    for antenna_type, locations in type_to_loc.items():
        for i in range(len(locations)):
            for j in range(len(locations)):
                if i != j:
                    draw_pair_harmonic(antenna_map, locations[i][0], locations[i][1], locations[j][0], locations[j][1])
    # print_map(antenna_map)
    ctr = count_antinodes(antenna_map)
    print(ctr)

def main():
    antenna_map = parse_input(inp)
    type_to_loc = find_antenna_locations(antenna_map)
    # print(antenna_map)
    # print(type_to_loc)
    part1(antenna_map, type_to_loc)
    part2(antenna_map, type_to_loc)
main()