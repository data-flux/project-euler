#!/usr/bin/env python3
"""
PROBLEM: 357
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    every n must be 1 lower than a prime and cannot be square
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy import divisors,primerange
from sympy.ntheory.primetest import is_square,isprime
from sys import stderr

def primegenerating(n):
    if is_square(n):
        return 0
    for div in divisors(n): #unfortunately a generator does not work, as it does not order the divisors, and we would break out of the loop too soon.
        if div*div>n:
            break
        if not isprime(div+(n//div)):
            return 0
    return n
                

if __name__=="__main__":
    tic()
    S=1 #1 gets skipped for being a square, but it counts.
    progress = 1_000_000
    for p in primerange(2,100_000_000):
        if p>progress:
            progress += 1_000_000
            eprint('.',end='')
        S += primegenerating(p-1)
    eprint()
    print(S)
    toc()
    exit()
