#!/usr/bin/env python3.6
""" 
PROBLEM: 001
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    - The sum of numbers [1,n] can be written as n*(n+1)/2
    - The sum of numbers below m divisible by a can thus be written as:
        - a*b*(b+1)/2
        - where b = ceil(m/a)-1
    - Since we add numbers divible by 15 twice, we subtract those again.
"""


from Euler.tictoc import *
from math import ceil

def sumOfDivByNUnderM(N,M):
    b = ceil(M/N)-1
    return int((b*(b+1)/2)*N)

if __name__=="__main__":
    tic()
    total = sumOfDivByNUnderM(3,1000) +\
            sumOfDivByNUnderM(5,1000) -\
            sumOfDivByNUnderM(15,1000)
    print(total)
    toc()
