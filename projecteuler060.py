#!/usr/bin/env python3.6
"""
PROBLEM: 060
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    guessed upper limit with some trial and error
    start at the top, as concatenated primes are more rare there.
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from Euler.primes import isprime
from Euler.digits import digitsToInt,intToDigits

def concatprime(p1,p2):
    d1 = intToDigits(p1)
    d2 = intToDigits(p2)
    c1 = digitsToInt(d1+d2)
    c2 = digitsToInt(d2+d1)
    return isprime(c1) and isprime(c2)

primes = [p for p in range(9000,2,-1) if isprime(p) and p!=5]

if __name__=="__main__":
    tic()
    for i1 in range(len(primes)):
        p1 = primes[i1]
        for i2 in range(i1+1,len(primes)):
            p2 = primes[i2]
            if concatprime(p1,p2):
                for i3 in range(i2+1,len(primes)):
                    p3 = primes[i3]
                    if concatprime(p1,p3) and concatprime(p2,p3):
                        for i4 in range(i3+1,len(primes)):
                            p4 = primes[i4]
                            if concatprime(p1,p4) and concatprime(p2,p4) and concatprime(p3,p4):
                                for i5 in range(i4+1,len(primes)):
                                    p5 = primes[i5]
                                    if concatprime(p1,p5) and concatprime(p2,p5) and concatprime(p3,p5) and concatprime(p4,p5):
                                        print(p1+p2+p3+p4+p5)
                                        toc()
                                        exit()
