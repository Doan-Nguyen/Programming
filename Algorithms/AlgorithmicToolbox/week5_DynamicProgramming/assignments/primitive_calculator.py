# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)
    


def primitive_calculator(n):
    '''
    c(n) = min(c(n/2) + 1 if n % 2 ==0)
    '''
    status = [0] * (n + 1)
    status[1] = 1
    #
    for i in range(2, n + 1):
        status_tmp = []
        if i % 2 == 0:
            status_tmp.append(status[i // 2] + 1)
        if i % 3 == 0:
            status_tmp.append(status[i // 3] + 1)
        # else:
        status_tmp.append(status[i - 1] + 1)
        status[i] = min(status_tmp)
    #
    ptr = n
    optimal_seq = [ptr]
    while ptr != 1:
        values = []
        if ptr % 3 == 0:
            values.append(ptr // 3)
        if ptr % 2 == 0:
            values.append(ptr // 2)
        values.append(ptr - 1)
        #
        ptr = min(
            [(c, status[c]) for c in values],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(ptr)
    return reversed(optimal_seq)


n = int(input())
# primitive_calculator(n)
sequence = list(primitive_calculator(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
