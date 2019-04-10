#!/usr/bin/env python3.6
"""
PROBLEM: 007
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    library solution
"""

from Euler.tictoc import *
from gmpy import next_prime

if __name__=="__main__":
    tic()
    n = 10_001
    x=1
    for i in range(n):
        x = next_prime(x)
    print(x)
    toc()
    exit()
