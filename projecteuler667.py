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
from math import sin,acos,pi,cos,sqrt

if __name__=="__main__":
    tic()
    theta = lambda x: acos(x[1]/(2*x[0]))
    phi =   lambda x: acos(x[0]/(2*x[1]))
    alpha = lambda x: pi - 2*theta(x)
    beta =  lambda x: pi - 2*phi(x)
    area1 = lambda x: x[0]*x[0]*sin(alpha(x))/2.
    area2 = lambda x: x[1]*x[1]*sin(beta(x))/2.
    objec = lambda x: -area1(x) - 2*area2(x)

    cons = ({'type':'ineq', 'fun': lambda x: 1-x[1]*sin(phi(x)+theta(x))},
            {'type':'ineq', 'fun': lambda x: 1-x[0]*cos(pi+phi(x)+alpha(x))},
            {'type':'ineq', 'fun': lambda x: 1-x[1]*cos(pi+2*phi(x)+alpha(x))},
            {'type':'ineq', 'fun': lambda x: x[1]-x[0]},
            {'type':'ineq', 'fun': lambda x: 2*x[0]-x[1]},
            #{'type':'ineq', 'fun': lambda x: 1-x[0]},
            )
    
    res = minimize(objec,(1.0,1.5), 
            bounds=((0.0,None),(0.0,None)),
            constraints=cons,
            tol = 1e-18,
            options = { 'maxiter': 10_000_000,
                        'disp': True,
                        'gtol': 1e-18},
            method = 'SLSQP'
        )
    x = res.x


    print(f"{x[0]:.10f}  {x[1]: .10f}")
    print(f"{(lambda x: x[1]*sin(phi(x)+theta(x)))(x):.10f}") #CONSTRAINT
    print(f"{(lambda x: x[0]*cos(pi+phi(x)+alpha(x)))(x):.10f}") #CONSTRAINT
    print(f"{(lambda x: x[1]*cos(pi+2*phi(x)+alpha(x)))(x):.10f}") #CONSTRAINT
    print(f"{area1(x)+2*area2(x):.10f}")



    toc()
    exit()
