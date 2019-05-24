def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

def totient(n):
    s = {i for i in range(1,n)}
    for a in range(1,n):
        if a not in s:
            continue
        g = gcd(n,a)
        if g>1:
            s -= set(range(g,n,g))
    return len(s)
