#!/usr/bin/env python3.6
"""
PROBLEM: 076
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    adapted problem #31
"""

from Euler.tictoc import *


if __name__=="__main__":
    tic()
    N = 100
    elements = range(1,N)
    ways = {rem: 0 for rem in range(0,N+1)}
    ways[0] = 1
    for c in elements:
        for remaining in range(c,N+1):
            if c>remaining:
                continue
            ways[remaining] += ways[remaining-c]
    print(ways[N])
    toc()
    exit()
