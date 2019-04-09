from time import time
GLOBAL_TIME = time()
def tic():
    t = time()
    GLOBAL_TIME = t
    return t

def toc(t=GLOBAL_TIME):
    elapsed = time() - t
    print("Elapsed time is %.6f seconds." % elapsed)
    return elapsed
