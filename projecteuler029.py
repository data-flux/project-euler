#!/usr/bin/env python3.6
"""
PROBLEM: 029
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    python set
"""

from Euler.tictoc import *

if __name__=="__main__":
    tic()
    s = {pow(a,b) for a in range(2,101) for b in range(2,101)}
    print(len(s))
    toc()
    exit()
