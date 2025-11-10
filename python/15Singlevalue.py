import numpy as np
n=int(input("Enter the order (n) of the square matrix : "))
print(f"Enter the elements of the order {n} x {n} matrix row-wise")
matrix=[]
for i in range(n):
    row=list(map(float,input().split()))
    matrix.append(row)

A=np.array(matrix)
U,S,VT=np.linalg.svd(A)
print("\n Matrix U : ")
print(U)
print("\n Singular values (s) : ")
print(S)
print("\n matrix VT : ")
print(VT)

S_matrix=np.zeros((n,n))
np.fill_diagonal(S_matrix,S)


A_reconstructed = U @ S_matrix @ VT
print("\n Reconstructed Matrix : ")
print(A_reconstructed)