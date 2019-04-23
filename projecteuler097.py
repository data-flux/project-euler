#!/usr/bin/env python3.6
"""
PROBLEM: 097
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    python does exponential modulus
"""

from Euler.tictoc import *

if __name__=="__main__":
    tic()
    a = 28_433
    b = pow(2,7_830_457,10**10)
    print((a*b+1)%(10**10))
    toc()
    exit()
