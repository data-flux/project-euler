#!/usr/bin/env python3.6
"""
PROBLEM: 012
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    divisors does not increase predictably, so no better search strategy than brute force.
"""

from Euler.tictoc import *
from sympy import divisor_count

if __name__=="__main__":
    tic()
    triangle = lambda x: x*(x+1)//2
    i=10000 #arbitrarily large starting, to save some time.
    d = 0
    while d<500:
        i += 1
        d = divisor_count(triangle(i))
    print(triangle(i))

    toc()
    exit()
