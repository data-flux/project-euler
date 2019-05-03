#!/usr/bin/env python3.6
"""
PROBLEM: 036
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    we look for palindromic numbers less than 1e6,
        cbaabc or cbabc, where abc % 2 != 0 (to prevent leading zeros in base 2)
    and a quick check in binary representation.
"""

from Euler.tictoc import *
from Euler.digits import intToDigits,digitsToInt,palindromic
from math import ceil,log2

def palindromicInBinary(n):
    binary = bin(n)[2:]
    for a,b in zip(binary,reversed(binary)):
        if a!=b:
            return False
    return True


if __name__=="__main__":
    tic()
    S = 0
    for i in range(1,1000,2):
        digits = intToDigits(i)
        p = digitsToInt(list(reversed(digits))+digits) #even length: cbaabc
        if palindromicInBinary(p):
            S += p
        p = digitsToInt(list(reversed(digits))+digits[1:]) #odd length: cbabc
        if palindromicInBinary(p):
            S += p
        if i<100: #center zeros: cb00bc
            p = digitsToInt(list(reversed(digits))+[0]+digits) 
            if palindromicInBinary(p):
                S += p
            p = digitsToInt(list(reversed(digits))+[0,0]+digits) 
            if palindromicInBinary(p):
                S += p
        if i<10: #center zeros: cb00bc
            p = digitsToInt(list(reversed(digits))+[0,0,0]+digits) 
            if palindromicInBinary(p):
                S += p
            p = digitsToInt(list(reversed(digits))+[0,0,0,0]+digits) 
            if palindromicInBinary(p):
                S += p
    print(S)
    toc()
    exit()
