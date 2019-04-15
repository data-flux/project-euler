#!/usr/bin/env python3.6
"""
PROBLEM: 025
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    memoization 101
"""

from Euler.tictoc import *
from functools import lru_cache
from math import log10

@lru_cache(maxsize=None)
def fib(a,b):
    return (b,a+b)

if __name__=="__main__":
    tic()
    a=b=1
    i = 2
    while log10(b) <= 999:
        a,b = fib(a,b)
        i += 1
    print(i)
    toc()
    exit()
