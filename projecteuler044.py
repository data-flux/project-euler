#!/usr/bin/env python3.6
"""
PROBLEM: 044
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    P(n) = n(3n-1)/2
    Find j and k such that
        P(j) + P(k) is pentagonal
    and P(j) - P(k) is pentagonal,
    and the difference is minimized.
    
    obviously j>k
    P(j)+P(k) = P(s)
    where s>j>k
    P(j)-P(k) = P(d)
    where d<j

    P(s) = s(3s-1)/2 == j(3j-1)/2 + k(3k-1)/2
        3s² - s == 3j²-j + 3k³-k
        for (7,4):
        3*64 - 8 == 3*49 - 7 + 3*16 - 4

    Since we want to minimise D=j-k, it is not clear what j and k we should be looking at.
    
    Incidentally, the first solution found is correct.

"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint

pent = lambda n: n*(3*n-1)//2

if __name__=="__main__":
    tic()
    found = set()
    for s in range(1,1_000_000_000):
        Ps = pent(s)
        for Pk in found:
            if Pk>Ps//2:
                continue
            if Ps-Pk in found:
                Pj = Ps-Pk
                if Pj-Pk in found:
                    print(Pj-Pk)
                    toc()
                    quit()
        found.add(Ps)
    exit()
