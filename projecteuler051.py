#!/usr/bin/env python3.6
"""
PROBLEM: 051
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    - last digits can't change, as we can't have primes ending in 0,2,5, leading to a maximum family size of 7.
    - we assume at least 2 numbers are getting changed.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from Euler.digits import digitsToInt,intToDigits
from sympy import sieve,primerange

def repeatingdigits(n):
    from math import floor,log10
    d = intToDigits(n)
    return len(set(d)) <= floor(log10(n))
        
def familysize(p):
    if not repeatingdigits(p):
        return 1
    dig = intToDigits(p)
    bestfamily = [p]
    for oldd in set(dig)-{dig[-1]}:
        family = [p]
        if len([d for d in dig if d==oldd])<2:
            continue
        for newd in set(range(10))-{oldd}:
            if newd==0 and dig[0]==oldd:
                continue
            newp = digitsToInt([newd if d==oldd else d for d in dig])
            if newp in sieve:
                family.append(newp)
        if len(family)>len(bestfamily):
            bestfamily = family
    for pr in bestfamily:
        memoize[pr] = len(bestfamily)
    if len(bestfamily)==8:
        print(bestfamily)
    return len(bestfamily)



if __name__=="__main__":
    tic()
    memoize = {p:None for p in primerange(5e4,5e5)}
    for p in primerange(5e4,5e5):
        if memoize[p]:
            continue
        if familysize(p)==8:
            break
    print(p)
    toc()
    exit()
