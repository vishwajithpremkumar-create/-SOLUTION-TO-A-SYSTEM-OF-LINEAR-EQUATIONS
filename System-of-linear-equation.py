#Program to find the solution for the given linear equations.
#Developed by:Vishwajith 
#RegisterNumber:25017437
import numpy as np
a=np.array([[1,-3],[3,1]])
b=np.array([0,10])
result=np.linalg.solve(a,b)
print(result)
