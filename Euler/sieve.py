class Sieve:
    def __init__(self,limit=1000):
        self.primes = []
        self.max_seen = 1
        self.extend(limit)

    def extend(self,limit):
        cndd = list(range(self.max_seen+1,limit+1))
        for p in self.primes:
            start = cndd[0] - (cndd[0] % p) + p
            for c in range(start,limit+1,p):
                try:
                    cndd.remove(c)
                except:
                    continue
        self.primes += cndd
        self.max_seen = limit
