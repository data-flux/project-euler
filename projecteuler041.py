#!/usr/bin/env python3.6
"""
PROBLEM: 041
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    educated guess on upper bound
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy import sieve
from Euler.digits import pandigital

if __name__=="__main__":
    tic()
    best = 0
    for prime in sieve:
        if prime>1e7:
            break
        if pandigital(prime):
            best = prime
    print(best)
    toc()
    exit()
