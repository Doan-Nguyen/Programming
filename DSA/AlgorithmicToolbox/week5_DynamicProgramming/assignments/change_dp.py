# Uses python3
import sys


def get_change(m):
    #   write your code here
    v = [1, 3, 5]
    min[0] = 0
    for i in range(1, m):
        for j in range(len(v) - 1):
            if v[j] <= i and (i - v[j]) + 1 < (i):
                i = i - v[j] + 1
    return m // 4


if __name__ == '__main__':
    m =  
    print(get_change(m))
