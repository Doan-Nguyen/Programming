def input_values():
    '''
    reference: 
    https://github.com/anoubhav/Coursera-Algorithmic-Toolbox/blob/master/assignment%20solutions/3.2%20maxloot.py
    '''
    # Python3
    n = int(input())
    list_1 = [int(i) for i in input().split()]
    list_2 = [int(i) for i in input().split()]
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)
    #
    return list_1, list_2


if __name__ == "__main__":
    list_1, list_2 = input_values()
    max_value = 0
    for i in range(len(list_1)):
        max_value += list_1[i]*list_2[i]
    print(max_value)