#!/usr/bin/env python3
"""
    integer partition function according to recurrence relation:
    p(0) = 1
    p(n<0) = 0
    p(n) = (-1)**(k-1) * p(n-k(3k-1)/2) for all k!=0
    formula and bounds for k taken from wikipedia.
"""

class Partition:
    def __init__(self,max=1):
        self.mem = {}
        self.max = 0
        self.extend(max)
        self.max = max

    def __getitem__(self,n):
        if n<0:
            return 0
        if n==0:
            return 1
        if n in self.mem.keys():
            return self.mem[n]
        from math import sqrt,floor,ceil
        p = 0
        for k in range(ceil(-(sqrt(24*n+1)-1)/6),floor((sqrt(24*n+1)+1)/6)+1):
            if k==0:
                continue
            p += int((-1)**(k+1)) * self[n-k*(3*k-1)//2]
        self.mem[n] = p
        return p

    def extend(self,max):
        for n in range(self.max,max+1):
            self[n]

if __name__=="__main__":
    print(Partition()[100])
