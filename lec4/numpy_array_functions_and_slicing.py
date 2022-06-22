import numpy as np
array = np.array([list(range(1, 11)), list(range(1, 11))])
print(array.shape)
print(array.dtype)
print(np.zeros(7))

print(np.zeros((4, 6)))

print(np.ones(7))
print(np.ones(7).dtype)

print(np.empty(5))

#arithmatic operation

print(array + array)
print(array - array)
print(array * array)
print(array / array)
print(1 / array)

#slicing

array2 = np.array(list(range(1,9)))
print(array2)
print(array2[4:7])
arr = array2[4:7]
print(arr)
#reference (pointer)
arr[0] = 15
print(array2)

#new array object
arrr = array2[4:7].copy()
arrr[0] = 31
print(arrr)
print(array2)

#slicing n dimentional array. in this xase, dimension 2
print(array[0])
print(array[0, 7])
