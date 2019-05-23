#!/usr/bin/env python3
"""
PROBLEM: 064
AUTHOR:  Dirk Meijer
STATUS:  in-progress
EXPLANATION:
    As soon as a_i is equal to 2*a_0, the period is starts over.
    fails on 139 and 151 currently.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy.ntheory.primetest import is_square
from math import sqrt,floor
from itertools import count


def periodic(a):
    if 2*a[0] != a[-1]: 
        return False
    l = len(a)//2+1
    for (s1,s2) in zip(a[1:l],a[-2:l-1:-1]):
        if s1!=s2:
            return False
    return True


def sqrtperiod(n):
    if is_square(n): 
        return 0
    a0 = floor(sqrt(n))
    a = [a0]
    r = (1,a0)
    for period in count(1):
        denom = n-r[1]*r[1]
        a.append(floor(r[0]*(sqrt(n)+r[1])/denom))
        r = (denom//r[0], (a[-1]*denom-r[0]*r[1])//r[0])
        if periodic(a):
            #print(f"p({n}) = {period}")
            return period

if __name__=="__main__":
    tic()
    print(sum(sqrtperiod(n)%2==1 for n in range(10_001)))
    toc()
    exit()
