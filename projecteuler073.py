#!/usr/bin/env python3.6
"""
PROBLEM: 073
AUTHOR:  Dirk Meijer
STATUS:  needs-optimization
EXPLANATION:
    pretty slow, but intuitive and clean.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from fractions import Fraction as F

if __name__=="__main__":
    tic()
    upper = 12000
    fractions = {F(n,d) for d in range(2,upper+1) for n in range(d//3,d//2+1) if 1/3 < n/d < 1/2}
    print(len(fractions))
    toc()
    exit()
