#!/usr/bin/env python3.6
"""
PROBLEM: 033
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    answers will be of the form ab/bd=a/d or ba/db=a/d
"""

from Euler.tictoc import *
from sympy import lcm,S
from functools import reduce
from operator import mul

prod = lambda l: reduce(mul,l,1)

if __name__=="__main__":
    tic()
    fractions = []
    for b in range(1,10):
        for d in range(1,10):
            for a in range(1,d):
                if 9*a*d + (-10*a + d) * b  == 0:
                    print(("%d%d/%d%d"%(a,b,b,d)))
                    fractions.append(S("%d%d/%d%d"%(a,b,b,d)))

                if 9*a*d + (10*b-a)*b == 0:
                    print(("%d%d/%d%d"%(b,a,d,b)))
                    fractions.append(S("%d%d/%d%d"%(b,a,d,b)))
    
    print("Product:\n",prod(fractions))
    toc()
    exit()
