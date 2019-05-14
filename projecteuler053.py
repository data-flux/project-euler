#!/usr/bin/env python3.6
"""
PROBLEM: 053
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    scipy combinatorics
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from scipy.misc import comb

if __name__=="__main__":
    tic()
    S=0
    for n in range(23,101):
        for k in range(1,n+1):
            S += comb(n,k)>1e6
    print(S)
    toc()
    exit()
