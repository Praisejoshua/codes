A=[[4,1], [8,3]]
B=[[9,6], [3,2]]
C=[[0,0], [0,0]]

C[0][0]= A[0][0] * B[0][0] + A[0][1] * B[1][0]
C[0][1]= A[0][0] * B[0][1] + A[0][1] * B[1][1]
C[1][0]= A[1][0] * B[0][0] + A[1][1] * B[1][0]
C[1][1]= A[1][0] * B[0][1] + A[1][1] * B[1][1]
print(C)
