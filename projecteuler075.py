#!/usr/bin/env python3.6
"""
PROBLEM: 075
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    pythagorean triples:
        a = k(m² - n²)
        b = 2*k*m*n
        c = k(m² + n²)
        L = 2*k*m*(m+n)
    triangle inequality states that c <= a+b, so c <= L/2
    we also have to keep track of solutions to avoid adding duplicates.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from math import sqrt

if __name__=="__main__":
    tic()
    Lmax = 1_500_000
    options = [set() for _ in range(Lmax+1)]
    for k in range(1,Lmax//10+1): #because m²+n² >= 5 and triangle inequality
        for m in range(2,int(sqrt(Lmax/(k*2)))+1): #also triangle inequality
            for n in range(1,m):
                L = 2*k*m*(m+n)
                if L <= Lmax:
                    a = k*(m*m-n*n)
                    b = 2*k*m*n
                    options[L].add((min(a,b),max(a,b)))
    print(sum(map(lambda x: len(x)==1,options)))
    toc()
    exit()
