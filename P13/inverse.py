import numpy as np 

x = np.array([[8,2,8], [-1,-1,8], [1,8,6]])
y = np.linalg.inv(x) 
print("X:\n", x)
print("X inverse:\n", y)
print("Dot calculation:\n",np.dot(x,y))