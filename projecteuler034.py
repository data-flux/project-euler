#!/usr/bin/env python3.6
"""
PROBLEM: 034
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    pythonic
"""

from Euler.tictoc import *
from Euler.digits import intToDigits
from math import factorial

if __name__=="__main__":
    tic()
    print(sum([n for n in range(10,100000) if n==sum(map(factorial,intToDigits(n)))]))
    toc()
    exit()
