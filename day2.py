inp = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

def make_matrix():
    matrix = []
    for line in inp.split('\n'):
        # print(line)
        row = []
        for elem in line.split():
            row.append(int(elem))
        matrix.append(row)
    return matrix

def count_num_safe(matrix):
    safe_rows = 0
    ret_unsafe_rows = []
    for row in matrix:
        monotiny = "X"
        safe = True
        for i in range(len(row)-1):
            if monotiny == "X":
                if row[i+1] > row[i]:
                    monotiny = "I"
                elif row[i+1] < row[i]:
                    monotiny = "D"
                else:
                    safe = False
                    break
            if monotiny == "I":
                diff = abs(row[i+1] - row[i])
                if row[i+1] < row[i] or diff < 1 or diff > 3:
                    safe = False
                    break
            else:
                diff = abs(row[i+1] - row[i])
                if row[i+1] > row[i] or diff < 1 or diff > 3:
                    safe = False
                    break
        if safe:
            # print(row)
            safe_rows += 1
        else:
            ret_unsafe_rows.append(row)
    return (safe_rows, ret_unsafe_rows)

matrix = make_matrix()
safe_rows, unsafe_rows = count_num_safe(matrix)
print(len(unsafe_rows))
for row in unsafe_rows:
    # print(row)
    for i in range(len(row)):
        elem = row.pop(i)
        # print(row)
        safe, _ = count_num_safe([row])
        if safe == 1:
            safe_rows += 1
            print(row)
            break
        row.insert(i, elem)
print(safe_rows)
