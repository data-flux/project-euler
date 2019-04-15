#!/usr/bin/env python3.6
"""
PROBLEM: 026
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    it's going to be a prime number, and to avoid cyclic patterns we return the first we find. Then to avoid too small patterns, we start the length at 10.
"""

from Euler.tictoc import *
from sympy import sieve,S,N

if __name__=="__main__":
    tic()
    sieve.extend(1000)
    primes = list(sieve._list)
    decimals = 5000
    best = 0
    bestp = 0
    for p in primes:
        s = str(N(1/S(p),decimals))[-2:1:-1]
        for l in range(10,decimals//4):
            if s[0:l] == s[l:2*l] == s[2*l:3*l] == s[3*l:4*l]:
                if l > best:
                    best = l
                    bestp = p
                break

    print(bestp)
    toc()
    exit()
