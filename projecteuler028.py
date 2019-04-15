#!/usr/bin/env python3.6
"""
PROBLEM: 028
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    first spiral has interval of 2, second of 4, third of 6, etc.
"""

from Euler.tictoc import *

if __name__=="__main__":
    tic()
    i = 1
    s = 1
    for spiral in range(1,501):
        for corner in range(4):
            i += spiral*2
            s += i
    print(s)
    toc()
    exit()
