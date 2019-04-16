from builtins import list

import numpy as np
#fx=[12,16,25,45,32,21,46,55,52,75,33,64]
#fx=[12,16,25,45,32,21,46,55,52,75,33]
#x=[0,1,2,3,4,5,6,7,8,9,10]
#x=[0,1,2,3,4,5,6,7,8,9,10,11]
x=[1,4,5]
fx=[0,1.38,1.60]
def diferDiv_recu(dato,x): # con esto hayaremos los b0 b1 b2
    if(len(x)==1):
        #index = np.where(x == x[0])
        return dato[x[0]]
        #return dato[index[0]]
    else:
        w=x[1:] #me elimina el primer elemento
        y=x[:-1] #me elimina el ultimo elemento
        return (diferDiv_recu(dato,w)-diferDiv_recu(dato,y))/(x[len(x)-1]-x[0])

#print(diferDiv_recu(fx,x))

def diferdiv_sqr(x,y,t):
    n=np.zeros((len(y),t+1),dtype=np.float64)
    for i in range(len(y)):
        n[i][0]=y[i]
    for k in range(1, t+1):
        for j in range (k,t+1):
            n[j][k]=(n[j][k-1]-n[j-1,k-1])-n[j-1,k-1]/(x[j]-x[j-k])
    return n
b=(diferdiv_sqr(x,fx,len(x)-1))

def newton_m(n,b,x):# newton con matrix
    sum=0
    for i in range(len(x)):
            sum=b[i][i]*multiplicatoria(i,n,x)
    return sum
def multiplicatoria(limit,n,x):
    mul=1
    for i in range(limit):
        mul=mul*(n-x[i])
    return mul
res=newton_m(2,b,x)
print(res)