#!/usr/bin/env python3.6
"""
PROBLEM: 668
AUTHOR:  Dirk Meijer
STATUS:  needs-optimization
EXPLANATION:
    answer should be correct, but takes too much time and memory to calculate.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy import sieve
from math import sqrt




lim = 10**7
sqrtlim = int(sqrt(lim))

gen = set()
S = 1

def nextgen():
    global gen,S
    #eprint(gen)
    newgen = set()
    S += len(gen)
    for n in gen:
        for p in sieve.primerange(1,min(sqrtlim,lim//n+1)):
            newgen.add(p*n)
    del gen
    gen = newgen 

if __name__=="__main__":
    tic()
    sieve.extend(sqrtlim)
    for p1 in sieve.primerange(1,sqrtlim):
        for p2 in sieve.primerange(p1,min(sqrtlim,lim//p1+1)):
            if p1*p2 > lim:
                break
            for p3 in sieve.primerange(p2,min(sqrtlim,lim//(p1*p2)+1,p1*p2+1)):
                gen.add(p1*p2*p3)
    while len(gen)>0:
        nextgen()        
    print(S)
    toc()
    exit()
