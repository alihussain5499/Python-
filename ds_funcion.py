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