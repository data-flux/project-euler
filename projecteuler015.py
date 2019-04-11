#!/usr/bin/env python3.6
"""
PROBLEM: 015
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    library solution
"""

from Euler.tictoc import *
from sympy import binomial

if __name__=="__main__":
    tic()
    print(binomial(40,20))
    toc()
    exit()
