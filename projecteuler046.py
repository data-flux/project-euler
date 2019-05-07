#!/usr/bin/env python3.6
"""
PROBLEM: 046
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    straightforward with educated guess on upper limit
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy import primerange,sieve
from math import floor,sqrt

if __name__=="__main__":
    tic()
    lastlim = 9
    currentlim = 10000
    found = False
    while not found:
        twicesquares = {i*i for i in range(1,floor(sqrt(currentlim/2))+1)}
        for n in range(lastlim,currentlim,2):
            if n in sieve:
                continue
            solution = False
            for p in primerange(3,n+1):
                if (n-p)//2 in twicesquares:
                    solution = True
                    break
            if not solution:
                print(n)
                toc()
                exit()
        lastlim = currentlim-1
        currentlim *= 10
