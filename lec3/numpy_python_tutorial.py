import numpy as np
array = np.arange(100000)
pythList = list(range(100000))

"""for _ in range(1000):
    array = array * 3"""

array2 = np.array([x for x in range(1, 1001)])
#object introspection
print(id(array2))
print(type(array2))
print(array2)
