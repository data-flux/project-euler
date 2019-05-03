#!/usr/bin/env python3.6
"""
PROBLEM: 043
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    ugly pos that works
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from Euler.digits import digitsToInt

if __name__=="__main__":
    tic()
    S=0
    d=[None]*10
    for d789 in range(17,987,17):
        d[7] = d789//100
        d[8] = (d789//10)%10
        d[9] = d789%10
        if d[7]==d[8] or d[7]==d[9] or d[8]==d[9]:
            d[7:] = [None]*3
            continue
        for d6 in [i for i in range(10) if i not in d]:
            d[6] = d6
            if digitsToInt(d[6:9])%13 != 0:
                d[6] = None
                continue
            for d5 in [i for i in [0,5] if i not in d]:
                d[5] = d5
                if digitsToInt(d[5:8])%11 != 0:
                    d[5] = None
                    continue
                for d4 in [i for i in range(10) if i not in d]:
                    d[4] = d4
                    if digitsToInt(d[4:7])%7 != 0:
                        d[4] = None
                        continue
                    for d3 in [i for i in range(0,10,2) if i not in d]:
                        d[3] = d3
                       #if digitsToInt(d[3:6])%5 != 0:  #not necessary because d5 is 0 or 5
                       #    d[3] = None
                       #    continue
                        for d2 in [i for i in range(10) if i not in d]:
                            d[2] = d2
                            if digitsToInt(d[2:5])%3 != 0:
                                d[2] = None
                                continue
                            for d1 in [i for i in range(10) if i not in d]:
                                d[1] = d1
                               #if digitsToInt(d[1:4])%2 != 0: #not necessary because d3 is even
                               #    d[1] = None
                               #    continue
                                d[0] = [i for i in range(10) if i not in d][0]
                                eprint(digitsToInt(d))
                                S += digitsToInt(d)
                                d[0] = None
                                d[1] = None
                            d[2] = None
                        d[3] = None
                    d[4] = None
                d[5] = None
            d[6] = None
        d[7] = None
        d[8] = None
        d[9] = None
    
    print(S)
    toc()
    exit()
