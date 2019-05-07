#!/usr/bin/env python3.6
"""
PROBLEM: 047
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    bruteforce
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy import factorint

if __name__=="__main__":
    tic()
    n = 647
    while True:
        f1 = set(factorint(n).keys())
        if len(f1)<4:
            n+=1
            continue
        f2 = set(factorint(n+1).keys())
        if len(f2)<4:
            n+=2
            continue
        if len(f2-f1)<4:
            n+=1
            continue
        f3 = set(factorint(n+2).keys())
        if len(f3)<4:
            n+=3
            continue
        if len(f3-f2)<4:
            n+=2
            continue
        f4 = set(factorint(n+3).keys())
        if len(f4)<4:
            n+=4
            continue
        if len(f4-f3)<4:
            n+=3
            continue
        print(n)
        toc()
        exit()
