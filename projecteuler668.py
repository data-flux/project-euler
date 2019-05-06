#!/usr/bin/env python3.6
"""
PROBLEM: 668
AUTHOR:  Dirk Meijer
STATUS:  experimentation
EXPLANATION:
    answer should be correct, but takes about 24h to calculate.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy import sieve
from math import sqrt

lim = 10_000_000_000
sqrtlim = int(sqrt(lim))

S = 1 #because we're not generating 1
gen = set()

def nextgen():
    global gen,S
    #print(gen)
    newgen = set()
    S += len(gen)
    for n,maxprime in gen:
        for p in sieve.primerange(1,sqrtlim):
            if n*p > lim:
                break
            newgen.add((n*p,max(maxprime,p)))
    gen = newgen

if __name__=="__main__":
    tic()
    sieve.extend(sqrtlim)
    for p1 in sieve.primerange(1,sqrtlim):
        for p2 in sieve.primerange(p1,sqrtlim):
            for p3 in sieve.primerange(p2,sqrtlim):
                a = p1*p2*p3
                if a <= 100 and p3*p3<a:
                    gen.add((a,p3))
    while len(gen)>0:
        nextgen()        
    print(S)
    toc()
    exit()
