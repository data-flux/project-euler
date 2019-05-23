#!/usr/bin/env python3.6
"""
PROBLEM: 065
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    fractions package allows us to keep generating.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from fractions import Fraction as f
from itertools import islice
from Euler.digits import intToDigits

def gen():
    i = 2
    while True:
        yield 1
        yield i
        yield 1
        i += 2

if __name__=="__main__":
    tic()
    convergents = reversed(list(islice(gen(),99)))
    F = f(1,next(convergents))
    for c in convergents:
        F = f(1,c+F)
    F=2+F
    print(sum(intToDigits(F.numerator)))
    toc()
    exit()
