#!/usr/bin/env python3.6
"""
PROBLEM: 017
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    not that hard, just annoying.
"""

from Euler.tictoc import *

atoms = {0: 0,
         1: 3,
         2: 3,
         3: 5,
         4: 4,
         5: 4,
         6: 3,
         7: 5,
         8: 5,
         9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8,
        20: 6,
        30: 6,
        40: 5,
        50: 5,
        60: 5,
        70: 7,
        80: 6,
        90: 6,
       100: 7,
      1000: 8}


def wordlength(n):
    if n<20: 
        return atoms[n]                                         #eg: eleven
    if n<100: 
        return atoms[10*(n//10)]+atoms[n%10]                    #eg: forty two
    if n<1000:
        if n%100 == 0:
            return atoms[n//100]+atoms[100]                     #eg: two hundred
        return atoms[n//100]+atoms[100]+3+wordlength(n%100)     #eg: two hundred and forty two
    return 3 + atoms[1000]                                      #eg: one thousand

if __name__=="__main__":
    tic()
    print(sum(map(wordlength,range(1,1001))))
    toc()
    exit()
