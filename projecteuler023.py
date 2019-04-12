#!/usr/bin/env python3.6
"""
PROBLEM: 023
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    sympy solution, set comprehension to save time
"""

from Euler.tictoc import *
from sympy import divisors


if __name__=="__main__":
    tic()

    abundant = lambda n: sum(divisors(n)) > 2*n #because sympy.divisors adds n as a divisor of n
    to_check = range(28124)
    abundant_numbers = [n for n in to_check if abundant(n)]

    abundant_sums = {abundant_numbers[i] + abundant_numbers[j] for i in range(len(abundant_numbers)) for j in range(i,len(abundant_numbers))}

    non_abundant_sums = {i for i in to_check if i not in abundant_sums}

    print(sum(non_abundant_sums))

    toc()
    exit()
