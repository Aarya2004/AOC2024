orders = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

updates = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def make_orders(order):
    return order.split()
    
def correct_order(inp, order_list):
    elem_list = []
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            if inp[j]+'|'+inp[i] in order_list:
                return False
    return True

def part1(update_list, orders_list):
    correct_updates = []
    for update in update_list:
        if correct_order(update, orders_list):
            correct_updates.append(update)
    print(correct_updates)
   
    s = 0
    for update in correct_updates:
        s += int(update[len(update)//2])
    print(s)
    print('-----------------')

def correct_the_order(inp, order_list):
    elem_list = []
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            if inp[j]+'|'+inp[i] in order_list:
                temp = inp[i]
                inp[i] = inp[j]
                inp[j] = temp
    if not correct_order(inp, order_list):
        inp = correct_the_order(inp, order_list)
    return inp

def part2(update_list, orders_list):
    incorrect_updates = []
    for update in update_list:
        if not correct_order(update, orders_list):
            incorrect_updates.append(update)
    print(incorrect_updates)
   
    for i in range(len(incorrect_updates)):
       incorrect_updates[i] = correct_the_order(incorrect_updates[i], orders_list)
    
    s = 0
    for update in incorrect_updates:
        s += int(update[len(update)//2])
    print(s)
    print('-----------------')

def main():
    orders_list = make_orders(orders)
    print(orders_list)
    print('-----------------')
    update_list = [update.split(',') for update in updates.split()]
    print(update_list)
    print('-----------------')
    part1(update_list, orders_list)
    part2(update_list, orders_list)
