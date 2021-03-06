#!/usr/bin/env python3.6
"""
PROBLEM: 015
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    library solution
"""

from Euler.tictoc import *
from Euler.digits import intToDigits

if __name__=="__main__":
    tic()
    print(sum(intToDigits(2**1000)))
    toc()
    exit()
