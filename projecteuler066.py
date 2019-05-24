#!/usr/bin/env python3.6
"""
PROBLEM: 066
AUTHOR:  Dirk Meijer
STATUS:  in-progress
EXPLANATION:
    for a given D, find the smallest solution in x for D=(x²-1)/y²
    x will always be larger than y
    find the value of D for with the largest smallest x
    (x²-1)/D must be square
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy.ntheory.primetest import is_square
from itertools import count
from math import sqrt

if __name__=="__main__":
    tic()
    best = 0
    bestD = 0
    for D in range(2,1001):
        if is_square(D):
            continue
        for y in count(1):
            if is_square(y*y*D+1):
                print(f"{int(sqrt(y*y*D+1)):6}² - {D:3} x {y:6}² = 1")
                if y*y*D>best:
                    best = y*y*D
                    bestD = D
                break
    print(bestD) 
    toc()
    exit()
