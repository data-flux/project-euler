#!/usr/bin/env python3.6
"""
PROBLEM: 005
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    factor each number into primes
    the maximum appearance of each prime multiplied is sufficient to divide all numbers.
"""

from Euler.tictoc import *
from Euler.sieve import Sieve

def primefactors(n,primes):
    ind = 0
    factors = {p: 0 for p in primes}
    while n>1:
        if ind == len(primes):
            raise Exception("prime list insufficient")
        if n % primes[ind] == 0:
            factors[primes[ind]] += 1
            n //= primes[ind]
        else:
            ind += 1
    return factors


if __name__=="__main__":
    tic()
    N = 20
    primes = Sieve(N).primes
    primefactors = [primefactors(i,primes) for i in range(1,N+1)]
    out = 1
    for p in primes:
        m = 0
        for f in primefactors:
            m = max(m,f[p])
        out *= pow(p,m)
    print(out)
    toc()
    exit()
