# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:12:53 2019

@author: ali hussain
"""
a=[10,20,30,40,50]
def amean(x):
    return sum(x)/len(x)
print(amean(a))

def gmean(x):
    n=len(x) 
    m=1
    for v in x:
        m*=v
    return m**(1/n)
print(gmean(a))

def hmean(x):
    n=len(x)
    s=sum([1/v for v in x])
    return n/s
print(hmean(a))

def means(x):
    am=amean(x)
    gm=gmean(x)
    hm=hmean(x)
    return (am,gm,hm)
means(a)
print(means(a))

def sd(x):
    avg=amean(x)
    num=sum([(v-avg)**2 for v in x])
    den=len(x)-1
    return num/den
sd(a)
b=[13,20,15,29,40]
c=[20,30,40,50,60]
def conv(x,y):
    avgx=amean(x)
    avgy=amean(y)
    dx=[v-avgx for v in x]
    dy=[v-avgy for v in y]
    dxy=[a*b for a,b in list(zip(dx,dy))]
    num=sum(dxy)
    den=len(x)-1
    return num/den
conv(a,b)
