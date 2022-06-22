import numpy as np

a = np.arange(1, 21)
print(a)

b = np.array([466,563,4,5,3,2,6,7,8,7,6,4,3,33,3,3,3,3,3,4,2,56,3,66,6,5,4,33,3,3,3,2,2,2,2,5,68,9,8,6,8,5,5,5,5,5,4])
print(b)
print(np.shape(b))
print(a.reshape(2, 10))

#argsort() method return indexes by which the array(matrix) element would be sorted in ascending order
print(np.argsort(b))

#argmin() method return argsort's first element(index)
print(np.argmin(b))

#argmax() method return argsort's last element(index)
print(np.argmax(b))

#argsort() in multidimensional array
print(np.argsort(a))
print(np.argsort(a, axis=0))
