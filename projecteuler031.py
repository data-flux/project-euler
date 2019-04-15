#!/usr/bin/env python3.6
"""
PROBLEM: 031
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    dynamic programming
"""

from Euler.tictoc import *


if __name__=="__main__":
    tic()
    coins = [200,100,50,20,10,5,2,1]
    ways = {rem: 0 for rem in range(0,201)}
    ways[0] = 1
    for c in coins:
        for remaining in range(c,201):
            if c>remaining:
                continue
            ways[remaining] += ways[remaining-c]
    print(ways[200])
    toc()
    exit()
