def input_values():
    '''
    reference: 
    https://github.com/anoubhav/Coursera-Algorithmic-Toolbox/blob/master/assignment%20solutions/3.2%20maxloot.py
    '''
    # Python3
    n, W = [int(i) for i in input().split()]
    lst = []

    if W == 0:
        print(0)
        quit()

    for _ in range(n):
        v, w = [int(i) for i in input().split()]
        if v == 0:
            continue
        lst.append((v, w))
    #
    lst.sort(key=lambda x: x[0], reverse=True)
    return lst, n, W


def maximum_value_of_loot(lst, n, W):
    numb_turn = n
    max_value = W
    print(numb_turn, max_value)
    # sorted by value
    value = 0
    c_turn = 0

    for item in lst[1:]:
        capacity_item = item[1]
        value_item = item[0]

        if item[1] <= max_value and c_turn < numb_turn:
            c_turn += max_value/capacity_item
            value += (max_value/capacity_item)*value_item
    return value


if __name__ == "__main__":
    lst, n, W = input_values()
    value = maximum_value_of_loot(lst, n, W)
    print(value)