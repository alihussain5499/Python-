import numpy as np
p=np.array([1,2,3,4,5])

p
p.shape

p.dtype

p=np.array([1,2,3.5,4,5],dtype='float')
p.dtype
p


p=np.array([1,2,3.5,4,5],dtype='complex')
p.dtype
p

p=np.array([[1,2],[3,4]])
p

p.shape

p=np.array([[[1,2,3],[3,4,5],[6,7,8]]])
p

p=np.array([[1,2,3],[3,4,5]])
p.reshape(6,1)

p.reshape(3,2)

p.reshape(1,6)

np.ones(shape=3)
np.zeros(2)

np.empty(5)


x = np.linspace(-np.pi, np.pi, 10)
print (x)

t=np.array((1,2,3))
t

t.size

t.ndim

t.sum()
t.argmin()

t.T

t.mean()

t1=np.arange(10)
t1

t1.reshape(5,2)

t1.reshape(2,5)

t1[2:3]

t1[2::5]

#t1[rows:columns,position]#
t2=t1.reshape(2,5)

t2[0:2,3]
t2[0:2,2]
t2[0:1,1]
t2[1:2,1]
t2
t2[0]
t2[1]
t2[1:,3]


























