#!/usr/bin/env python3.6
"""
PROBLEM: 004
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    The largest palindromic number will have 6 digits (cannot have 7 if > 1000*1000) so we generate 3 digit numbers, starting at 999, and find a palindromic one.
"""

from Euler.tictoc import *
from Euler.digits import palindromic


if __name__=="__main__":
    tic()
    m = 0
    for a in range(999,900,-1):
        for b in range(999,a,-1):
            if palindromic(a*b):
                m = max(m,a*b)
    print(m)
    toc()
