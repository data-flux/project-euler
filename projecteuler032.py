#!/usr/bin/env python3.6
"""
PROBLEM: 032
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    the # digits will always be [2]x[3]x[4] or [1]x[4]=[4] (rarely)
"""

from Euler.tictoc import *
from Euler.digits import digitsToInt,intToDigits

if __name__=="__main__":
    tic()
    solutions = set()

    m1 = [(a,b) for a in range(1,10) for b in range(1,10) if a!=b]
    m3 = [(a,b,c,d) for a in range(1,10) for b in range(1,10) for c in range(1,10) for d in range(1,10) if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d]
    for M3 in m3:
        N3 = digitsToInt(M3)
        for M1 in m1:
            pandigital = True
            for dig in M1:
                if dig in M3:
                    pandigital = False
                    break
            if not pandigital:
                continue
            N1 = digitsToInt(M1)
            if N3 % N1 != 0:
                continue
            N2 = N3 // N1
            if N2<123 or N2>987: #must be 3 digits
                continue
            M2 = intToDigits(N2)
            if 0 in M2:
                continue
            for ind,dig in enumerate(M2):
                if dig in M2[:ind] or dig in M2[ind+1:] or dig in M1 or dig in M3:
                    pandigital = False
                    break
            if pandigital:
                solutions.add(N3)
                print("%d x %d = %d"%(N1,N2,N3))


    m1 = [(a,) for a in range(1,10)]
    m3 = [(a,b,c,d) for a in range(1,10) for b in range(1,10) for c in range(1,10) for d in range(1,10) if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d]
    for M3 in m3:
        N3 = digitsToInt(M3)
        for M1 in m1:
            pandigital = True
            for dig in M1:
                if dig in M3:
                    pandigital = False
                    break
            if not pandigital:
                continue
            N1 = digitsToInt(M1)
            if N3 % N1 != 0:
                continue
            N2 = N3 // N1
            if N2<1234 or N2>9876: #must be 4 digits
                continue
            M2 = intToDigits(N2)
            if 0 in M2:
                continue
            for ind,dig in enumerate(M2):
                if dig in M2[:ind] or dig in M2[ind+1:] or dig in M1 or dig in M3:
                    pandigital = False
                    break
            if pandigital:
                solutions.add(N3)
                print("%d x %d = %d"%(N1,N2,N3))

    print(sum(solutions))
    toc()
    exit()
