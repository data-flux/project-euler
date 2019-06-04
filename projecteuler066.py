#!/usr/bin/env python3.6
"""
PROBLEM: 066
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    for a given D, find the smallest solution in x for D=(x²-1)/y²
    x will always be larger than y
    find the value of D for with the largest smallest x
    (x²-1)/D must be square

    y√D = √(x²-1)
    If we expand the fraction of D and multiply by y, we can turn the newly
    obtained expansion into an expansion for √(x²-1).
    Given the expansion, we look for the smallest y such that the expansion of
    √(D*y²) = (a0, [1, 2*a0])

    It is given that the minimum solution is some convergent of √D
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from itertools import count
from Euler.sqrt import sqrtconvergents
from sympy.ntheory.primetest import is_square
from sympy.ntheory.generate import primorial

def minX(D):
    if is_square(D):
        return 0
    for frac in sqrtconvergents(D):
        x = frac.numerator
        y = frac.denominator
        if x*x - D*y*y == 1:
            return x

if __name__=="__main__":
    tic()
    best = 0
    bestD = 0
    for D in range(1,1001):
        x = minX(D)
        if x>best:
            best = x
            bestD = D
    print(f"D = {bestD} ; x = {best}")
    toc()
    exit()
