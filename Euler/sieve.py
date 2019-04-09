#!/usr/bin/env python3.6

class Sieve:
    def __init__(self,limit=1000):
        self.primes = []
        self.max_seen = 1
        self.extend(limit)

    def extend(self,limit):
        if limit <= self.max_seen:
            raise ValueError("New Limit must be larger than existing limit!")
        cndd = list(range(self.max_seen+1,limit+1))
        for p in self.primes:
            start = cndd[0] - (cndd[0] % p) + p
            for c in range(start,limit+1,p):
                try:
                    cndd.remove(c)
                except:
                    continue
        while len(cndd)>0:
            p = cndd[0]
            cndd = cndd[1:]
            self.primes.append(p)
            if len(cndd)==0:
                break
            start = cndd[0] - (cndd[0] % p) + p
            for c in range(start,limit+1,p):
                try:
                    cndd.remove(c)
                except:
                    continue
        self.primes += cndd
        self.max_seen = limit

if __name__=="__main__":
    from tictoc import *
    tic()
    Sieve( 10_000)
    Sieve(100_000)
    toc()
    tic()
    s = Sieve(10_000)
    s.extend(100_000)
    toc()
