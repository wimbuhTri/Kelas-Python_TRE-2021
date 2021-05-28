import numpy as np

a = np.arange(9)
b = np.linspace(3,12,9)

a = a.reshape([3,3])
b = b.reshape([3,3])

c= np.dot(a,b)
print(c)

print(np.linalg.det(c))

print(np.transpose(a))