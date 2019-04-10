#!/usr/bin/env python3.6
"""
PROBLEM: 010
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    library solution
"""

from Euler.tictoc import *
from gmpy import next_prime

if __name__=="__main__":
    tic()
    n = 2_000_000
    x=1
    s=0
    while x < n:
        x = next_prime(x)
        s += x
    print(s)
    toc()
    exit()
