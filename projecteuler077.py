#!/usr/bin/env python3.6
"""
PROBLEM: 077
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    adapted problem #31
"""

from Euler.tictoc import *
from Euler.primes import isprime


if __name__=="__main__":
    tic()
    upper = 1000
    elements = [p for p in range(upper) if isprime(p)]
    for N in range(upper):
        ways = {rem: 0 for rem in range(0,N+1)}
        ways[0] = 1
        for c in elements:
            for remaining in range(c,N+1):
                if c>remaining:
                    continue
                ways[remaining] += ways[remaining-c]
        if ways[N] > 5_000:
            break
    print(N)
    toc()
    exit()
