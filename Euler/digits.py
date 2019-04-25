#!/usr/bin/env python3.6
from math import log10,floor

def intToDigits(n):
    if n <= 0:
        raise ValueError("Positive integers only!")
    d = floor(log10(n))+1
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

def pandigital9(n):
    digits = intToDigits(n)
    if len(digits)!=9:
        return False
    if not all(d in digits for d in range(1,9)):
        return False
    return True

if __name__ == "__main__":
    n = 5001
    print(n)
    print(intToDigits(n))
    print(digitsToInt(intToDigits(n)))
