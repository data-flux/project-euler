#!/usr/bin/env python3.6
"""
PROBLEM: 085
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    for H,B sizes of the grid, we can see that the amount of rectangles is:
        A = (H*(H+1)/2)*(B*(B+1)/2)
    solving for H:
        H = sqrt((1+16*A/(B²+B))/2)-1
    by taking the floor and ceiling for H, we find the closest solutions,
    iterate over B until H>=B, then we've reached symmetry.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from math import sqrt,ceil,floor

if __name__=="__main__":
    tic()
    A = 2_000_000
    B = 1
    bestdiff = 2_000_000
    bestBH = (0,0)
    while True:
        H = sqrt((1+16*A/(B*B+B)))/2-1
        if H<B:
            break
        for h in [floor(H),ceil(H)]:
            a = h*(h+1)*B*(B+1)//4
            if abs(A-a)<bestdiff:
                bestdiff = abs(A-a)
                bestBH = (B,h)
        B += 1

    print(bestBH[0]*bestBH[1])

    toc()
    exit()
