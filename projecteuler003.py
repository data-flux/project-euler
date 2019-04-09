#!/usr/bin/env python3.6
"""
PROBLEM: 003
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    Simple extendable sieve.
"""

from Euler.tictoc import *
from Euler.sieve import Sieve



if __name__=="__main__":
    tic()
    N = 600851475143
    sieve = Sieve(10000)

    ind = 0
    p = 0
    while N > 1:
        if N % sieve.primes[ind] == 0:
            p = sieve.primes[ind]
            N /= p
        else:
            ind += 1
            try:
                sieve.primes[ind]
            except:
                new_limit = sieve.max_seen*10
                print("Extending sieve to %d"%new_limit)
                sieve.extend(new_limit)
    print(p)



    toc()
    exit()
