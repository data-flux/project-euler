#!/usr/bin/env python3.6
"""
PROBLEM: 092
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    look ma, no proper tail call optimization!
"""

from Euler.tictoc import *
from Euler.digits import intToDigits
from functools import reduce

next = lambda n: reduce(lambda S,d: S+d*d,intToDigits(n),0)
memoize = [None]*10_000_001
memoize[1]=1
memoize[89]=89

def chain(*c):
    n = next(c[0])
    m=memoize[n]
    if m:
        for a in c:
            memoize[a] = m
        return
    else:
        chain(n,*c)
        

if __name__=="__main__":
    tic()
    for i in range(1,10_000_000):
        chain(i)
    print(sum(map(lambda i: i==89,memoize)))
    toc()
    exit()
