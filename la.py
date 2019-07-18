from mat import *

'''import sys
namefile1 = sys.argv[1]
namefile2 = sys.argv[2]
A = readm(namefile1)
b = readm(namefile2)'''

A = readm('A.csv')
b = readm('b.csv')
def solve(A, b):
    import numpy as np
    a,b = np.array(A), np.array(b)
    n= len(A[0])
    x = np.array([0]*n)

    for k in range(0, n-1):
        #1
        for j in range(k+1, n):
            if a[j,k] != 0.0:
                lam = a[j][k]/a[k][k]
                a[j,k:n] = a[j, k:n] - lam*a[k,k:n]
                b[j] = b[j] - lam*b[k]
        #2
    for k in range(n-1,-1,-1):
        #x[n-1] = b[n-1]/A[n-1][n-1]
        x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
    return x.flatten()


print(solve(A,b))

