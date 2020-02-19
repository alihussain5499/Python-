import math
math.ceil(4)
math.ceil(4.12)

math.floor(3)
math.floor(3.95)
math.floor(3.12)

math.sqrt(9)

math.exp(0)
math.exp(1)

math.log10(81)
math.log10(100)

math.pi

math.cos(360)
math.cos(180)

import random

random.random()
random.randrange(2,8)
random.randrange(2,8)

import os
os.mkdir("cse")
os.mkdir("cse1")

l=[]
for i in range(1,10):
    l.append(i**2)
print(l)    
    
l1=[i**2 for i in range(1,10)]
l1

l=[]
for i in range(1,4):
    for j in range(1,5):
        if(i!=j):
            l.append(i)
l

l1=[(i,j) for i in range(1,4) for j in range(1,5) if (i!=j)]
l1








