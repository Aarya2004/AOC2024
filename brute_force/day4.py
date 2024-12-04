inp = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

##PART 1

# Horizontal
def search_horz(matrix):
    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-3):
            if matrix[i][j:j+4] in ('XMAS','SAMX'):
                c += 1
    return c
    
def search_vert(matrix):
    c = 0
    for i in range(len(matrix)-3):
        for j in range(len(matrix[i])):
            string = matrix[i][j]
            for k in range(1,4):
                string += matrix[i+k][j]
            if string in ('XMAS','SAMX'):
                c += 1
    return c
    
def search_diag1(matrix):
    c = 0
    for i in range(3, len(matrix)):
        for j in range(len(matrix[i])):
            string = ''
            k = 0
            if j+4 > len(matrix[i]):
                break
            while i-k >= 0 and j+k < len(matrix[i]) and k < 4:
                string += matrix[i-k][j+k]
                k += 1
            ret = search_horz([string])
            if ret > 0:
                # print("I: " + str(i) + " J: " + str(j))
                c += ret
    return c
    
def search_diag2(matrix):
    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1-3, -1, -1):
            string = ''
            k = 0
            if i+3 > len(matrix):
                break
            while j+k < len(matrix[i]) and i+k < len(matrix[i]) and k < 4:
                string += matrix[i+k][j+k]
                k += 1
            ret = search_horz([string])
            if ret > 0:
                c += ret
    return c

def part1(matrix):       
    ctr = search_horz(matrix)
    ctr += search_vert(matrix)
    ctr += search_diag1(matrix)
    ctr += search_diag2(matrix)
    print(ctr)

##PART 2

def find_X(i,j,matrix):
    if matrix[i][j] == 'A':
        if matrix[i-1][j-1] == 'M' and matrix[i-1][j+1] == 'M':
            if matrix[i+1][j-1] == 'S' and matrix[i+1][j+1] == 'S':
                return True
        elif matrix[i-1][j-1] == 'M' and matrix[i+1][j-1] == 'M':
            if matrix[i-1][j+1] == 'S' and matrix[i+1][j+1] == 'S':
                return True
        elif matrix[i+1][j-1] == 'M' and matrix[i+1][j+1] == 'M':
            if matrix[i-1][j-1] == 'S' and matrix[i-1][j+1] == 'S':
                return True
        elif matrix[i+1][j+1] == 'M' and matrix[i-1][j+1] == 'M':
            if matrix[i+1][j-1] == 'S' and matrix[i-1][j-1] == 'S':
                return True
    return False
    
def search_X(matrix):
    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i-1 >= 0 and i+1 < len(matrix) and j-1 >= 0 and j+1 < len(matrix[i]) and \
                    find_X(i,j,matrix):
                c += 1
    return c

def part2(matrix):
    ctr = search_X(matrix)
    print(ctr)

def main():
    matrix = inp.split()
    part1(matrix)
    part2(matrix)
