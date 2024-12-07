import copy
inp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

guard_faces = ['^', '>', 'v', '<']

def make_matrix(inp):
    res = []
    for line in inp.split():
        res.append(list(line))
    return res
    
def find_start_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in guard_faces:
                return (i,j, matrix[i][j])

def move_straight(face):
    if face == '^':
        return (-1, 0)
    elif face == '>':
        return (0, 1)
    elif face == 'v':
        return (1, 0)
    else:
        return (0, -1)

def turn(face):
    if face == '<':
        return '^'
    return guard_faces[guard_faces.index(face)+1]
    
def make_moves(matrix, curr_x, curr_y, face):
    c = 0
    seen = []
    while True:
        move_x, move_y = move_straight(face)
        if curr_x+move_x >= len(matrix) or curr_y+move_y >= len(matrix) \
                or curr_x+move_x < 0 or curr_y+move_y < 0:
            break
        elif matrix[curr_x+move_x][curr_y+move_y] == '#':
            face = turn(face)
            continue
        matrix[curr_x+move_x][curr_y+move_y] = face
        matrix[curr_x][curr_y] = 'X'
        if (curr_x, curr_y) not in seen:
            c += 1
            seen.append((curr_x, curr_y))
        curr_x = curr_x+move_x
        curr_y = curr_y+move_y
    c += 1
    return c

def find_end(matrix, curr_x, curr_y, face):
    while 0 <= curr_x < len(matrix) and 0 <= curr_y < len(matrix[curr_x]) and matrix[curr_x][curr_y] != '#':
        move_x, move_y = move_straight(face)
        curr_x += move_x
        curr_y += move_y
    move_x, move_y = move_straight(face)
    curr_x -= move_x
    curr_y -= move_y
    return curr_x, curr_y

def check_loop(matrix, start_x, start_y, start_face):
    start = (start_x, start_y, start_face)
    curr_x, curr_y, face = start_x, start_y, start_face
    seen = []
    while True:
        move_x, move_y = move_straight(face)
        if curr_x+move_x >= len(matrix) or curr_y+move_y >= len(matrix) \
                or curr_x+move_x < 0 or curr_y+move_y < 0:
            break
        elif matrix[curr_x+move_x][curr_y+move_y] == '#':
            face = turn(face)
            continue
        # print(curr_x, curr_y)
        if (curr_x, curr_y, face) not in seen:
            seen.append((curr_x, curr_y, face))
        else:
            return True
        curr_x = curr_x+move_x
        curr_y = curr_y+move_y
    return False

def place_obstacle_clear_matrix(matrix, og_matrix, start_x, start_y, start_face):
    c = 0
    obstacles = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X' or matrix[i][j] in guard_faces:
                temp = og_matrix[i][j]
                og_matrix[i][j] = '#'
                print((i, j))
                if check_loop(og_matrix, start_x, start_y, start_face):
                    obstacles.append((i,j))
                    c += 1
                og_matrix[i][j] = temp
    print(obstacles)
    return c
    
def print_matrix(matrix):
    for line in matrix:
        print("".join(line))

def part1(matrix):
    start_x, start_y, start_face = find_start_pos(matrix)
    ctr = make_moves(matrix, start_x, start_y, start_face)
    print(ctr)
    print_matrix(matrix)

def part2(matrix, og_matrix):
    start_x, start_y, start_face = find_start_pos(og_matrix)
    ctr = place_obstacle_clear_matrix(matrix, og_matrix, start_x, start_y, start_face)
    print(ctr)
    
def main():
    matrix = make_matrix(inp)
    print_matrix(matrix)
    og_matrix = copy.deepcopy(matrix)
    part1(matrix)
    print_matrix(og_matrix)
    part2(matrix, og_matrix)
main()