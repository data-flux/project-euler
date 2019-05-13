#!/usr/bin/env python3  
"""
PROBLEM: 049
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    for any 2 primes that are permutations, check if the next in sequence is also
    a permutation and a prime.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from Euler.digits import ispermutation
from sympy import primerange,sieve

if __name__=="__main__":
    tic()
    for p1 in primerange(1489,9999): #assume lowest term is larger than given sequence
        for p2 in primerange(p1+1,1e4):
            if ispermutation(p1,p2) and p2+(p2-p1) in sieve and ispermutation(p1,p2+(p2-p1)):
                    print(f"{p1}{p2}{p2+(p2-p1)}")
                    toc()
                    exit()
