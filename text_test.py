# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows a tooltip on 
a window and a button

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import random
def shift(row):
    for i in range(1,N):
        if row[i-1] == 0:
            row.pop(i-1)
            break
        
        if row[i-1] == row[i] and row[i] > 2:
            row[i] *= 2
            row.pop(i-1)
            break
        
        if row[i-1]*row[i] == 2: # a pair of 1 and 2:
            row[i] = 3
            row.pop(i-1)
            break

    else:
        return False
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