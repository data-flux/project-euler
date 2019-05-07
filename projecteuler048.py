#!/usr/bin/env python3.6
"""
PROBLEM: 048
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    python pow modulo works great
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint

if __name__=="__main__":
    tic()
    mod = 10**10
    print(sum(pow(i,i,mod) for i in range(1,1000))%mod) #no need for the last one, all zeros
    toc()
    exit()
