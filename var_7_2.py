import math
def solve(sequence):
    sum_even_val = 0
    sum_odd_val = 0

    for i in range(1, len(sequence), 2):
        value = sequence[i]
        if value % 2 == 0:
            sum_even_val += value
        else:
            sum_odd_val += value
            
    return sum_even_val - sum_odd_val

seq = [1, 2, 3, 4, 5, 6, 7, 8]
print(solve(seq))
