from time import time
GLOBAL_TIME = time()
def tic():
    t = time()
    GLOBAL_TIME = t
    return t

def toc(t=GLOBAL_TIME):
    elapsed = time() - t
    if elapsed < .1:
        print("Elapsed time is %.1e seconds." % elapsed)
    else:
        print("Elapsed time is %.1f seconds." % elapsed)
    return elapsed
