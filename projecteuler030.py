#!/usr/bin/env python3.6
"""
PROBLEM: 030
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    brute force, arbitrary upperbound at 2e5
"""

from Euler.tictoc import *
from Euler.digits import intToDigits

if __name__=="__main__":
    tic()
    print(sum({n for n in range(1,200000) if sum(map(lambda d: pow(d,5),intToDigits(n)))==n}))
    toc()
    exit()
