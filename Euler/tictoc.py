from time import time
import sys
GLOBAL_TIME = time()
def tic():
    t = time()
    GLOBAL_TIME = t
    return t

def toc(t=GLOBAL_TIME):
    elapsed = time() - t
    if elapsed < .1:
        print("Elapsed time is %.1e seconds." % elapsed,file=sys.stderr)
    else:
        print("Elapsed time is %.1f seconds." % elapsed,file=sys.stderr)
    return elapsed
