#!/usr/bin/env python3.6
"""
PROBLEM: 021
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    sympy solution
"""

from Euler.tictoc import *
from sympy import divisors

divsum = lambda n: sum(divisors(n))-n  #sympy.divisors adds n as a divisor of n

if __name__=="__main__":
    tic()
    prev_found = set()
    S = 0
    for i in range(2,10000):
        if i in prev_found:
            continue
        j = divsum(i)
        if i!=j and divsum(j)==i:
            #print("Amicable pair: %d and %d"%(i,j))
            S += i+j
            prev_found.add(j)
    print(S)
    toc()
    exit()
