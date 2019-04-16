#!/usr/bin/env python3.6
"""
PROBLEM: 033
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    answers will be of the form ab/bd=a/d or ba/db=a/d, work these out for the equations on lines 21 and 25
"""

from Euler.tictoc import *
from functools import reduce
from fractions  import Fraction


if __name__=="__main__":
    tic()
    fractions = []
    for b in range(1,10):
        for d in range(1,10):
            for a in range(1,d):
                if 9*a*d + (-10*a + d) * b  == 0:
                    print(("%d%d/%d%d"%(a,b,b,d)))
                    fractions.append((a,d))

                if 9*a*d + (10*b-a)*b == 0:
                    print(("%d%d/%d%d"%(b,a,d,b)))
                    fractions.append((a,d))
    
    num,denom = reduce(lambda f1,f2:(f1[0]*f2[0],f1[1]*f2[1]),fractions,(1,1))
    print(Fraction(num,denom).denominator)
    toc()
    exit()
