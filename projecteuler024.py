#!/usr/bin/env python3.6
"""
PROBLEM: 024
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    sympy solution
"""

from Euler.tictoc import *
from Euler.digits import digitsToInt
from sympy.combinatorics import Permutation

if __name__=="__main__":
    tic()
    p=Permutation.unrank_lex(10,rank=1_000_000-1).array_form
    print(digitsToInt(p))
    toc()
    exit()
