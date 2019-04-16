import numpy as np
x=[1,3,5]
fx=[0,1.09,1.60]
def li(limit , x , n):
    mul=1
    for j in range(len(x)):
        if(j != limit):
            mul=mul*(n-x[j])/(x[limit]-x[j])
    return mul
def lagrange(dato,x,n):
    sum=0
    for i in range(len(x)):
        sum+=li(i,x,n)*dato[i]
    return sum
print(lagrange(fx,x,2))