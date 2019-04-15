#!/usr/bin/env python3.6
"""
PROBLEM: 027
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    n²+n+41 is a prime generating polynomial,
    by substituting m = (n-40), we get
        (n-40)² + (n-40) + 41
      =  n² -79n + 1601
    for any such substitution m = (n-c), we get c additional primes
    as such, we find the highest c for with b < 1000

      (n-c)² + (n-c) + 41
    = n² + (1-2c)n + 41 - c + c²
    such that
    a = 1-2c
    b = c² -c + 41
"""

from Euler.tictoc import *

if __name__=="__main__":
    tic()
    for c in range(40,-1,-1):
        b = c*c - c + 41
        if b < 1000:
            a = 1-2*c
            print(a*b)
            break
    toc()
    exit()
