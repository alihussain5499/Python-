import numpy as np
x=np.array([0,1,2,3,4])
x
x=np.arange(5)
x
y=x.reshape(5,1)
y
y.ravel()

a=np.array([1,2,3])
a

x=np.tile(a,(2,3))
x


x=np.tile(a,(2,4))
x


x=np.tile(a,(2))
x


x=np.tile(a,(1,3))
x

z=np.array([1,2,3])
print(z)
a=np.tile(z,(4,1))
print(a)


z=np.array([1,2,3])
print(z)
a=np.tile(z,(5,1))
print(a)


z=np.array([1,2,3])
print(z)
a=np.tile(z,(5,2))
print(a)


z=np.array([1,2,3])
print(z)
a=np.tile(z,(5,3))
print(a)


v=[[1,2],[
   3,4]]
x=[[5,6],[
   7,8]]

np.dot(v,x)

n=np.loadtxt("abc.txt",skiprows=1,unpack=True)
n


n=np.loadtxt("abc.txt",skiprows=2,unpack=True)
n


n=np.loadtxt("abc.txt",skiprows=1)
n


n=np.loadtxt("abc.txt",unpack=True)  #error #
n


n=np.loadtxt("abc2.txt",skiprows=1,unpack=False)
n

n=np.genfromtxt("abc2.txt",skip_header=1,filling_values=-999)
n


n=np.genfromtxt("abc2.txt",skip_header=1,filling_values=-0.9)
n


n=np.genfromtxt("abc2.txt",skip_header=1,filling_values=-9.99)
n


a=np.array[1,2,3]
np.savetxt("array.txt",a)

np.identity(1)

np.identity(5)

np.identity(4,dtype='int32')
np.identity(4,dtype='int')
np.identity(4,dtype='float')
















