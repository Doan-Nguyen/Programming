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
    lst.sort(key=lambda x: x[0]/x[1], reverse=True)
    return lst, n, W


def maximum_value_of_loot(lst, n, W):
    # max_value = W
    # # sorted by value
    # value = 0
    # for i in range(n):
    #     item = lst[i]
    #     if max_value >= item[1]:
    #         value += float(item[0])
    #     else:
    #         value += float(item[0]/item[1])*max_value
    #     max_value = max_value - item[1]
    # return round(value, 4)
    total_value = 0

    for v,w in lst:
        if W==0:
            print(total_value)
            quit()
        amt = min(w, W)
        total_value += amt*v/w
        W -= amt

    print(total_value)


if __name__ == "__main__":
    lst, n, W = input_values()
    value = maximum_value_of_loot(lst, n, W)
    # print(value)
    #
   