#!/usr/bin/env python3.6
"""
PROBLEM: 035
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    ezpz
"""

from Euler.tictoc import *
from sympy import sieve
from Euler.digits import intToDigits,digitsToInt

def rotations(n):
    dig = intToDigits(n)
    for i in range(1,len(dig)):
        yield digitsToInt(dig[i:]+dig[:i])


if __name__=="__main__":
    tic()
    sieve.extend(1e6)
    primes = {p for p in sieve._list if p<1e6}
    found = set()
    for p in primes:
        if p in found:
            continue
        rot = rotations(p)
        if all(map(lambda r: r in primes,rot)):
            found.add(p)
            for r in rot:
                found.add(r)
    print(len(found))
    toc()
    exit()
