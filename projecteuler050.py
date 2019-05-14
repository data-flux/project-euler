#!/usr/bin/env python3
"""
PROBLEM: 050
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    naive solution that searches for possible solutions at a high sequence length,
    then reduces that length when it fails to find a solution.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy import primerange


if __name__=="__main__":
    tic()
    upper = 1_000_000
    primes = list(primerange(1,upper))
    for seqlen in range(len(primes)//100,1,-1):
        for end in range(len(primes)//100,seqlen,-1):
            cs = sum(primes[end-seqlen:end])
            if cs<upper and cs in primes:
                print(cs)
                toc()
                exit()
