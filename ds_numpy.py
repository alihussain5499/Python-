# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:39:38 2019

@author: ali hussain
"""
################################################################################################################
# DAY 1
import numpy as np
x=np.array([10,20,30,40])
print(x)

y=x+100
print(y)

z=x+y
print(z)

a=np.arange(5)
print(a)

b=a+1
print(b)

np.ones(5)

np.zeros(5)

np.ones(10)*10

np.zeros(10)+20

np.array([1])

np.array([1]*10)

np.random.random(5)

np.random.seed(105)
np.random.random(5)

np.random.seed(100)
2*np.random.random(6)-1

np.random.randn(5)

a=np.array([10,20,30,40])
a=np.random.choice(a)
print(a)

np.random.choice(a,2)

a=np.arange(5)
print(a)

a+=10
b=a+100
c=a+b
d=a+b+c
m=np.c_[a,b,c]
print(m)

sal=[1000,2000,3000,4000,5000,9000]
sal=np.array(sal)
np.c_[sal,sal*0.1,sal*0.2]

z=np.zeros([5,2])
o=np.ones([5,2])
np.concatenate([z,o],axis=0)

np.concatenate([z,o],axis=1)

################################################################################################################
# DAY 2


import numpy as np
a=np.array([2,4,5,6,7,8])
b=np.array([4,9,11,6,8,9])
c=np.c_[a,b]
print(c)

a=np.arange(12)+1
b=np.reshape(a,(3,4))
print(b)

c=a.reshape((4,3))

np.ndim(a)

np.ndim(b)

c.ndim

np.shape(a)

b.shape

np.shape(c)

A=np.array([[10,20,30],[40,50,60]])
A.shape

B=(np.arange(30)+1).reshape(5,6)
print(B)

B[2,4]

B[1:4,2:-1]

B[1:3,2:-1]

B[2:,1:]

x=np.arange(45)+20
print(x)

# 3 market  :  hyd del pune
# 3 product :  tom oni crot
# 5 days    :  mon tue wed thu fri 

p=x.reshape((3,3,5))
print(p)

p.ndim

p.shape

p[0]

p[-1]

p[0,2]

p[1,1,2:]

p[1,:,1]

p[:,:,[1,3]]





A=np.array([[1,2],[3,4]])
print(A)

np.transpose(A)
# or
A.T
# or
A.transpose()

B=np.array([[2,5,6],[7,8,9]])
C=np.dot(A,B)
# or
C=A.dot(B)
print(C)

from numpy.linalg import inv
inv(A)

a=inv(A.T.dot(A)).dot(A.T.dot(B))
print(a)

################################################################################################################
# Day 3

import numpy as np

np.zeros((784,784*2,10))

np.random.random((784,1500,10))

A=np.array([[10,20,30],[30,30,60]])
print(A)
i=np.where(A>20)
print(i)
l=list(i[0])
r=list(i[1])
print(l)
print(r)
n=list(zip(l,r))
print(n)

np.random.seed(100)
a=(np.random.randint(5,size=90))*1000
print(a)

# 3 market , 2 shift , 3 product , 5 days

price=a.reshape((3,2,3,5))
print(price)
price.ndim
price.ravel()
price[0,1,2,4]
price[2]
price[1,1]
price[0,0,0]
price[0:-1,0,0:2,2:] 

np.where(price>20)

################################################################################################################
# Day 4

import numpy as np
a=np.array([10,20,30])
# Function for geometric mean
def gmean(x):
    n=x.size
    m=1
    for v in x:
        m*=v
    return m**(1/n)

gmean(a)
a.mean() # Predefine function for arithmetic mean

# Function for harmonic mean
def hmean(x):
    n=x.size
    d=(1/x).sum()
    return n/d
hmean(a)

# Function for all type of means
def means(x):
    am=x.mean()
    gm=gmean(x)
    hm=hmean(x)
    return (am,gm,hm)
means(a)

# Function for range
def range(x):
    return x.max() -x.min()

range(a)

# Varience of population
def varpop(x):
    return ((x-x.mean())**2).sum()/x.size
varpop(a)

# Varience for sample
def varsamp(x):
    return varpop(x)*x.size/x.size-1
varsamp(a)

# Standard deviation
def sdpop(x):                 # Standard deviation of population
    return varpop(x)**0.5

def sdsamp(x):                # Standard deviation of sample
    return varsamp(x)**0.5

sdpop(a)

sdsamp(a)

# Covarience
def cov(x,y):
    x=np.array(x)
    y=np.array(y)
    dx=x-x.mean()
    dy=y-y.mean()
    return (dx*dy).sum()/(x.size-1)

t=[10,20,25,30,40,5]
ice=[20,42,53,65,32,11]
swt=[100,50,20,5,2,140]

cov(t,ice)

cov(t,swt)
























