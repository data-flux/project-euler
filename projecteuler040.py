#!/usr/bin/env python3.6
"""
PROBLEM: 040
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    using a generator
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from Euler.digits import intToDigits
from itertools import islice
from functools import reduce
from operator import mul

def dig():
    yield 0
    for n in range(1,1_000_000):
        for d in intToDigits(n):
            yield d

if __name__=="__main__":
    tic()
    indices = [1,10,100,1000,10_000,100_000,1_000_000]
    digits = map(lambda i:next(islice(dig(),i,i+1)),indices)
    print(reduce(mul,digits,1))
    toc()
    exit()
