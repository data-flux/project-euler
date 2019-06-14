#!/usr/bin/env python3.6
"""
PROBLEM: 078
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    previous approaches didn't work anymore, implemented recurrence relation
"""

from Euler.tictoc import *
from Euler.partition import Partition
from itertools import count

if __name__=="__main__":
    tic()
    p = Partition()
    for n in count():
        if p[n] % 1_000_000 == 0:
            break
    print(n)
    toc()
    exit()
