from math import e, cos

def f(x:int,y:int,z:int):
    """Returns the value of f(x,y,x) function"""
    return 2*x*z*e**(-x)-2*y**3+y**2-3*z**3+(cos(x*z)/(1+e**(-x-y)))