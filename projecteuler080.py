#!/usr/bin/env python3
"""
PROBLEM: 080
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    wikipedia bullshit
"""

from Euler.tictoc import tic,toc
from itertools import islice,count

def sqrtdigits(n):
    pairs = []
    while n>0:
        pairs.append(n%100)
        n //= 100
    rem = 0
    p = 0
    c = rem*100+pairs[-1]
    pairs = pairs[:-1]
    while True:
        for x in count():
            if (x+1)*(20*p+x+1)>c:
                break
        yield x
        y = x*(20*p+x)
        p = p*10+x
        rem = c-y
        if rem == 0 and len(pairs)==0:
            return
        if len(pairs)==0:
            c=rem*100
        else:
            c = rem*100+pairs[-1]
            pairs = pairs[:-1]



    
    while True:
        yield 1

if __name__=="__main__":
    tic()
    total = 0
    prec = 100
    for n in range(1,100): #exclude 100 as it's not irrational
        total += sum(islice(sqrtdigits(n),0,prec))
    total -= sum(range(1,10)) #subtract rational square roots, minus 100 which we didn't use and has a digit sum of 1
    print(total)
    toc()
    exit()
