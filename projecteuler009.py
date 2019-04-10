#!/usr/bin/env python3.6
"""
PROBLEM: 009
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    generating pythagorean triplets:
    m > n
    a = m² - n²
    b = 2*m*n
    c = m² + n²

    We are looking for:
    a + b + c = 1000 = 2m² + 2*m*n
    m*(m+n) = 500
    Since m>n, we are looking for a 2-term product a*b = 500, where 1 < b/a < 2
    The divisors of 500 are:
    { 1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250, 500 }
    We know that there is only 1 solution, and it must be 20*25

    therefore:
        m = 20
        n = 5
        a = 400 - 25 = 375
        b = 200
        c = 400 + 25 = 425

    a*b*c = 375*200*425
"""

from Euler.tictoc import *

if __name__=="__main__":
    tic()
    print(375*200*425)
    toc()
    exit()
