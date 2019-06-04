#!/usr/bin/env python3.6
"""
PROBLEM: 071
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    look for fractions close to 3/7 only.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from fractions import Fraction as F

if __name__=="__main__":
    tic()
    upper = 1_000_000
    fractions = {F(n,d) for d in range(2,upper+1) for n in range((3*d)//7,(3*d)//7+1) if n/d < 3/7}
    print(max(fractions))
    toc()
    exit()
