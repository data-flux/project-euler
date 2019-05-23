#!/usr/bin/env python3
"""
PROBLEM: 063
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    ezpz
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from Euler.digits import intToDigits
from math import log

if __name__=="__main__":
    tic()
    S = 0 
    for exponent in range(1,25):
        for base in range(1,25):
            n = pow(base,exponent)
            d = len(intToDigits(n))
            if d == exponent:
                S += 1
            if d > exponent:
                break
    print(S)
    toc()
    exit()
