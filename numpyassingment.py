#1#
import numpy as np
a=np.array([[[[1,2,3],[5,6,7],[9,7,1],[5,2,7]]]])
a
b=np.array([1,2,3])
b

c=a+b
c

b=np.array([[[1],[2],[3]]])
z=np.tile(b,(4,1))
z
c=a+z
c
#finding rank #
a=np.array([[1,2,3],[5,6,7],[9,7,1],[5,2,7]])
a
np.linalg.matrix_rank(a)


a=np.array([[1,2,9],[6,3,5]])
a.sort()
a

a=np.array([1,2,3,4,5,6,7,8])
np.amax(a)

a=np.array([[[1,2],[3,4],[5,6]]])
a
z=a.flatten()
y=list(z)
y[2:]


np.linspace(2,5,num=8)

np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
x = np.array([1,2,3], dtype=np.float64)
x.itemsize

x = np.array([1,2,3], dtype=np.complex128)
x.itemsize

x = np.array([1,2,3], dtype=np.int32)
x.itemsize

a = np.array([1,2,3])
b = np.array([0,1,0])
np.inner(a, b)







