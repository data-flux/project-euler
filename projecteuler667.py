#!/usr/bin/env python3.6
"""
PROBLEM: 667
AUTHOR:  Dirk Meijer
STATUS:  experimentation
EXPLANATION:
    3 isosceles triangles
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from sympy import S,tan,acos,sqrt,N

if __name__=="__main__":
    tic()
    theta1 = acos(0.5/sqrt(2))
    h1 = tan(theta1)/2
    b1 = 1
    theta2 = acos(sqrt(1/2))
    h2 = sqrt(1/2)*tan(theta2)
    b2 = sqrt(2)
    area = h1*b1+0.5*h2*b2
    print(N(area,12))
    toc()
    exit()
