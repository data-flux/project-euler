#!/usr/bin/env python3.6
"""
PROBLEM: 037
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    given that there are 11, keep searching until we've found eleven.
    could be sped up by building up instead of truncating down, probably
    this is because the primes cannot contain 2's except in the first digit,
    for example
"""

from Euler.tictoc import tic,toc
from Euler.digits import intToDigits,digitsToInt
from Euler.eprint import eprint
from sympy import sieve

def truncatable(prime):
    dig = intToDigits(prime)
    for i in range(1,len(dig)):
        trunc_r = digitsToInt(dig[:i])
        if trunc_r not in sieve:
            return False
        trunc_l = digitsToInt(dig[i:])
        if trunc_l not in sieve:
            return False
    return True


if __name__=="__main__":
    tic()
    found = 0
    S = 0
    for prime in sieve:
        if prime<10:
            continue
        if truncatable(prime):
            print(prime)
            found +=1
            S += prime
            if found == 11:
                break
    eprint(f"Total: {S}")
    toc()
    exit()
