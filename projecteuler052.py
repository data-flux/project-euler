#!/usr/bin/env python3.6
"""
PROBLEM: 052
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    first digit must be a one.
    assuming unique digits.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from Euler.digits import intToDigits,digitsToInt

def repeatingdigits(n):
    from math import floor,log10
    d = intToDigits(n)
    return len(set(d)) <= floor(log10(n))

if __name__=="__main__":
    tic()
    for x_ in range(10**4,10**7):
        dig = [1]+intToDigits(x_)
        x = digitsToInt(dig)
        if repeatingdigits(x):
            continue
        if sorted(intToDigits(2*x))==sorted(dig):
            if sorted(intToDigits(3*x))==sorted(dig):
                if sorted(intToDigits(4*x))==sorted(dig):
                    if sorted(intToDigits(5*x))==sorted(dig):
                        if sorted(intToDigits(6*x))==sorted(dig):
                            print(x)
                            toc()
                            exit()
