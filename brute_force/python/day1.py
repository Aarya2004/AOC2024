inp = '''3   4
4   3
2   5
1   3
3   9
3   3'''

i = 0
lst = inp.split()
lst1 = []
lst2 = []
occurences_in_lst2 = {}
# print(lst)
while i < len(lst):
    lst1.append(int(lst[i]))
    lst2.append(int(lst[i+1]))
    i += 2
# Part 1
lst1.sort()
lst2.sort()
s = 0
for j in range(len(lst1)):
    s += abs(lst1[j]-lst2[j])
print(s)

# Part 2
for item in lst2:
    if item not in occurences_in_lst2:
        occurences_in_lst2[item] = 1
    else:
        occurences_in_lst2[item] += 1
s = 0
for item in lst1:
    if item in occurences_in_lst2:
        s += item * occurences_in_lst2[item]
print(s)
