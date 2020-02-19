# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:58:21 2019

@author: ali hussain
"""
#Denormalization

m=open("D:/mystuff/manager.txt")
lines=m.readlines()
mngrs=lines[1:]

#dictionary

mdict={}
for line in mngrs:
    mid=line.strip().split(",")[0]
    mdict[mid]=line
print(mdict)    
    
d=open("D:/mystuff/dept1.txt")
dept=d.readlines()
dept=dept[1:]
ddict={}
for line in dept:
    w=line.strip().split(",")
    dno=w[0]
    ddict[dno]=line
for k in ddict:
    print(k,ddict[k])



e=open("D:/mystuff/emp2.txt")
emp=e.readlines()
emp=emp[1:]
print(len(emp))

out=open("D:mystuff/edm.txt","w")

for line in emp:
    w=line.strip().split(",")
    dno=w[-1]
    dinfo=ddict[dno]
    mid=dinfo.split(",")[-1]
    minfo=mdict[mid]
    dline=",".join(dinfo.split(",")[1:-1])
    newline=line.strip()+","+dline+","+minfo+"\n"
    out.write(newline)
out.close()    
    
    
    
    