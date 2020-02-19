# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:37:54 2019

@author: ali hussain
"""

#List
l=[10,20,30,40,50]
l

sum(l)

len(l)

avg=sum(l)/len(l)
avg

#accecing list element
# 1st by index number
l[0]

l[-1]

l[len(l)-1]

l[len(l)-2]

#2nd by slicing
l[1:4]

l[0:5]

l[:]

l[0:]

l[:5]

l[0:5:2]

l[-2:]

l.append(60)
l

m=[70,80,90]
l+m

l+=m
l

10 in l

100 in l

100 not in l

#Fitter
#way 1
p=[]
for v in l:
    if v>50:
        p.append(v)
        
print(p)

#way 2   [expr for loop  if condition]
q=[v for v in l if v>50  ]
q    

#Transformation over list ie same operation on each element of list
#way 1
a=[10,20,30,40,50,60]
b=[]
for v in a:
    b.append(v+100)
b    
   
#way 2
b=[v+1000 for v in a]
b


#tuple
t=("be","cse",2019,7.6)
t

#dictionary
d={101:"ali",102:"vijay",103:"sahn"}
d

d[101]

d[104]="aalu"
d