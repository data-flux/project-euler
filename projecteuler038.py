#!/usr/bin/env python3.6
"""
PROBLEM: 038
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    will have to be a digit starting with 9,
    will have to be smaller than 10000, to satisfy n>1
"""

from Euler.tictoc import tic,toc
from Euler.digits import pandigital9,intToDigits,digitsToInt

def concatproduct(n):
    digits = []
    for i in range(1,10):
        digits += intToDigits(n*i)
        if len(digits)>=9:
            break

    if pandigital9(digitsToInt(digits)):
        return digitsToInt(digits)
    return 0

if __name__=="__main__":
    tic()
    searchspace =   [9] +\
                    list(range(90,100)) +\
                    list(range(900,1000)) +\
                    list(range(9000,10000))
    print(max(map(concatproduct,searchspace)))
    toc()
    exit()
