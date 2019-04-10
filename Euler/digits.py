#!/usr/bin/env python3.6
from math import log10,ceil

def intToDigits(n):
    if n <= 0:
        raise ValueError("Positive integers only!")
    d = ceil(log10(n))
    digits = d*[None,]
    for b in range(d-1,-1,-1):
        digits[b] = n%10
        n //= 10
    return digits

def digitsToInt(digits):
    d = len(digits)
    out = sum([pow(10,i)*digits[b] for i,b in enumerate(range(d-1,-1,-1))])
    return out

def palindromic(n):
    digits = intToDigits(n)
    return digits == list(reversed(digits))

if __name__ == "__main__":
    n = 5001
    print(n)
    print(intToDigits(n))
    print(digitsToInt(intToDigits(n)))
