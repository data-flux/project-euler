#!/usr/bin/env python3.6
"""
PROBLEM: 667
AUTHOR:  Dirk Meijer
STATUS:  experimentation
EXPLANATION:
    3 isosceles triangles
"""

from Euler.tictoc import tic,toc
from Euler.eprint import eprint
from scipy.optimize import minimize,NonlinearConstraint
from math import sin,acos

if __name__=="__main__":
    tic()
    theta = lambda x: acos(x[1]/(2*x[0]))
    phi =   lambda x: acos(x[0]/(2*x[1]))
    area1 = lambda x: 0.5*x[0]*x[0]*sin(theta(x))
    area2 = lambda x: 0.5*x[1]*x[1]*sin(phi(x))
    objec = lambda x: -area1(x) - 2*area2(x)

    cons = ({'type':'ineq', 'fun': lambda x: 1-x[1]*sin(phi(x)+theta(x))},
            {'type':'ineq', 'fun': lambda x: x[1]-x[0]},
            )
    
    res = minimize(objec,(1.,1.), 
            bounds=((0.0,1.0),(0.0,None)),
            constraints=cons,
            tol = 1e-15,
            options = { 'maxiter': 10_000_000,
                        'disp': True}
        )

    print(f"{res.x[0]:.10f}  {res.x[1]: .10f}")
    #print(f"{(lambda x: x[1]*sin(phi(x)+theta(x)))(res.x):.10f}") #CONSTRAINT
    print(f"{-objec(res.x):.10f}")



    toc()
    exit()
