#!/usr/bin/env python3.6
"""
PROBLEM: 020
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    python handles this just fine.
"""

from Euler.tictoc import *
from math import factorial

if __name__=="__main__":
    tic()
    print(sum(map(int,str(factorial(100)))))
    toc()
    exit()
