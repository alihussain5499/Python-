# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:20:29 2018

@author: ali hussain
"""


a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))


if(a>b):
    min1=a
else:
    min1=b
    
    
while(True):
    if(min1%a==0 and min1%b==0):
        print("LCM is ",min1)
        break
    
    min1+=1
    
gcd=(a*b)/min1  

print("HCF is",gcd)  
    