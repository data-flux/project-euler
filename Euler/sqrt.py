from sympy.ntheory.primetest import is_square
from math import sqrt,floor
from itertools import count
from fractions import Fraction as f

def periodic(a):
    if 2*a[0] != a[-1]: 
        return False
    l = len(a)//2+1
    for (s1,s2) in zip(a[1:l],a[-2:l-1:-1]):
        if s1!=s2:
            return False
    return True


def sqrtperiod(n):
    if is_square(n) and int(sqrt(n))==sqrt(n): 
        return (int(sqrt(n)),[])
    a0 = floor(sqrt(n))
    a = [a0]
    r = (1,a0)
    for period in count(1):
        denom = n-r[1]*r[1]
        a.append(floor(r[0]*(sqrt(n)+r[1])/denom))
        r = (denom//r[0], (a[-1]*denom-r[0]*r[1])//r[0])
        if periodic(a):
            return (a[0],a[1:])

def sqrtconvergents(n):
    a0,period = sqrtperiod(n)
    p = len(period)
    yield f(a0,1)
    if p==0:
        return
    for terms in count():
        frac = f(1,period[terms%p])
        for t in range(terms-1,-1,-1):
            frac = f(1,period[t%p]+frac)
        yield a0 + frac
        

