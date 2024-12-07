import re

inp = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
seen = 0
s = 0
mult_active = True
for i in range(len(inp)-4):
    # print("seen: " + str(seen))
    if inp[i:i+2] == 'do':
        if i+4 < len(inp) and inp[i+2:i+4] == '()':
            mult_active = True
        elif i+7 < len(inp) and inp[i+2:i+7] == 'n\'t()':
            mult_active = False
    if i <= seen:
        continue
    if inp[i:i+4] == 'mul(' and mult_active:
        j = i+4
        operand1 = ''
        # print("j: " + inp[j])
        while inp[j].isdigit() and j < len(inp):
            operand1 += inp[j]
            j += 1
        if inp[j] != ',' or len(operand1) == 0 or j > len(inp):
            continue
        j = j + 1
        operand2 = ''
        while inp[j].isdigit() and j < len(inp):
            operand2 += inp[j]
            j += 1
        if inp[j] != ')' or len(operand2) == 0 or j > len(inp):
            continue
        seen = j
        print(operand1 + " * " + operand2)
        s += int(operand1) * int(operand2)
    else:
        seen = i
print(s)
