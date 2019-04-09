#!/usr/bin/env python3.6
"""
PROBLEM: 002
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    Tracking the sum while counting.
"""

from Euler.tictoc import *

def fibonacci_even(upper_limit=4e6):
    a = 1
    b = 2
    S = 2
    while True:
        a,b = b,a+b
        if b > upper_limit:
            return S
        if b % 2 == 0:
            S+=b
    

if __name__=="__main__":
    tic()
    print(fibonacci_even())
    toc()
    exit()
