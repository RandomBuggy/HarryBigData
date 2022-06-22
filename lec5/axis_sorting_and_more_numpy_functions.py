import numpy as np

a = np.array([[1, 2, 3],
    [4, 5, 6]])
#numpy array has two axis. axis 0 is column-wise, axis 1 is row-wise
print(a.sum(axis=0))
print(a.sum(axis=1))

#dot product of two matrix

b = np.array([[3, 6, 9], [7, 8, 0]])

print(a.dot(b.transpose()))

#cross product

print(np.cross(a, b))

#sorting
print(np.sort([7, 3, 5, 2, 4, 8, 1]))
print(np.sort([7, 3, 5, 2, 4, 8, 1], axis=0, kind="mergesort"))
