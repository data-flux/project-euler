#!/usr/bin/env python3
"""
PROBLEM: 062
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    straightforward search.
    knowing the lower limit reduces search time, but taking a naive approach
    takes almost 2 minutes.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from Euler.digits import ispermutation,intToDigits


if __name__=="__main__":
    tic()
    lower=4000
    upper=10000
    for n1 in range(lower,upper):
        c1 = n1*n1*n1
        dig = len(intToDigits(c1))
        for n2 in range(n1+1,upper):
            c2 = n2*n2*n2
            if len(intToDigits(c2)) > dig:
                break
            if not ispermutation(c1,c2):
                continue
            for n3 in range(n2+1,upper):
                c3 = n3*n3*n3
                if len(intToDigits(c3)) > dig:
                    break
                if not ispermutation(c2,c3):
                    continue
                for n4 in range(n3+1,upper):
                    c4 = n4*n4*n4
                    if len(intToDigits(c4)) > dig:
                        break
                    if not ispermutation(c3,c4):
                        continue
                    for n5 in range(n4+1,upper):
                        c5 = n5*n5*n5
                        if len(intToDigits(c5)) > dig:
                            break
                        if not ispermutation(c4,c5):
                            continue
                        print(c1)
                        toc()
                        exit()

