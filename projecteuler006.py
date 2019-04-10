#!/usr/bin/env python3.6
"""
PROBLEM: 006
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    only count the crossterms, and count them twice
"""

from Euler.tictoc import *

if __name__=="__main__":
    tic()
    N = 100
    crossterms = [(a,b) for a in range(1,N+1) for b in range(a+1,N+1)]
    print(sum([2*a*b for a,b in crossterms]))
    toc()
    exit()
