# -*- coding: utf-8 -*-

import random
def shift(row):
    for i in range(N-1):
        if row[i] == 0:
            break
        if row[i] == row[i+1] and row[i] > 2:
            row[i+1] *= 2
            break
        if row[i]*row[i+1] == 2: # a pair of 1 and 2:
            row[i+1] = 3
            break
    else:
        return False
    row.pop(i)
    row.append(0)
    return True

N = 4
# [1,2]+[3*2**i for i in range(4)]
tiles = [1, 2, 3]

row = [0 for c in range(N)]
count = 0
print(row)
while shift(row) and count<20:
    row[-1] = random.choice(tiles)
    print(row)
    count += 1
print(count)