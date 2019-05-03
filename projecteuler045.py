#!/usr/bin/env python3.6
"""
PROBLEM: 045
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    easier than 44.
    Tn < Pn < Hn, so we find the second n for which Tn also appears in P and H.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint

tria = lambda n: n*(n+1)//2
pent = lambda n: n*(3*n-1)//2
hexa = lambda n: n*(2*n-1)


if __name__=="__main__":
    tic()
    P = set()
    H = set()
    for n in range(285,1_000_000): #starting point is lucky, 143 is safe though.
        Tn = tria(n)
        if Tn in P and Tn in H:
            print(Tn)
            if Tn>40755:
                toc()
                quit()
        P.add(pent(n))
        H.add(hexa(n))
    exit()
