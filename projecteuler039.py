#!/usr/bin/env python3.6
"""
PROBLEM: 039
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    for k>0, m>n>0:
        a = k*(m*m - n*n)
        b = k*(2*m*n)
        c = k*(m*m + n*n)
    p = a+b+c
      = k*2*m*(m+n)

    find p<=1000 that maximizes the #solutions
    
    tracking solutions in sets, because (a,b,c) are not ordered for ordered (k,m,n)
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from math import sqrt

if __name__=="__main__":
    tic()
    MAXVAL = 1000
    solutions = [set() for i in range(MAXVAL+1)]
    for k in range(1,MAXVAL//12+1):
        for m in range(2,int(sqrt(MAXVAL/(2*k)))+1):
            for n in range(1,m):
                p = 2*k*m*(m+n)
                if p<MAXVAL:
                    a,b,c = sorted((k*(m*m - n*n),k*2*m*n, k*(m*m - n*n)))
                    solutions[p].add((a,b,c))

    best = solutions.index(max(solutions,key=len))
    print(best)
    toc()
    exit()
