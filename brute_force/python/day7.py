import copy
inp = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def get_equations(inp):
    return inp.split('\n')

def get_operands_and_result(equation):
    ret = equation.split()
    ret[0] = ret[0][:-1]
    return ret

def count_valid_equations(equation, part):
    operands = get_operands_and_result(equation)
    # print("Evaluating Expr: " + operands[0])
    eq_result = int(operands.pop(0))
    last_result = []
    for operand in operands:
        if not last_result:
            last_result.append(int(operand))
        else:
            prev_values = copy.deepcopy(last_result)
            last_result.clear()
            for value in prev_values:
                if value+int(operand) <= eq_result:
                    last_result.append(value+int(operand))
                if value*int(operand) <= eq_result:
                    last_result.append(value*int(operand))
                if part == 2:
                    if int(str(value)+str(operand)) <= eq_result:
                        last_result.append(int(str(value)+str(operand)))

    for result in last_result:
        if result == eq_result:
            return eq_result
    return False


def part1(incomplete_equations):
    ctr = 0
    for equation in incomplete_equations:
        val = count_valid_equations(equation, 1)
        if val:
            ctr += val
    print(ctr)

def part2(incomplete_equations):
    ctr = 0
    for equation in incomplete_equations:
        val = count_valid_equations(equation, 2)
        if val:
            ctr += val
    print(ctr)

def main():
    incomplete_equations = get_equations(inp)
    print(incomplete_equations)
    part1(incomplete_equations)
    part2(incomplete_equations)
    
main()