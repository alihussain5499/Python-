# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:53:24 2019

@author: ali hussain

"""
################################################################################################################
#Day 1

f=open("D:/mystuff/comment.txt")
line1=f.readline().split()
line2=f.readline()
line3=f.readline()
print(line1)
print(line2)
print(line3)


f=open("D:/mystuff/comment.txt")
line4=f.readlines()
print(line4)
print("_"*20)
for v in line4:
    print(v)


f2=open("D:/mystuff/samp2.txt")
head=f2.readline()
lines=f2.readlines()
tot=0
cnt=0
for v in lines:
    w=v.strip().split(',')
    sal=int(w[-1])
    tot+=sal
    cnt+=1
print("Total salary ",tot) 
print("Average salary ",tot/cnt)   



f2=open("D:/mystuff/samp2.txt")
head=f2.readline()
lines=f2.readlines()
sal=[]
for v in lines:
    w=v.strip().split(',')
    sal.append(int(w[-1]))
    
def aggregatn(x):
    tot=sum(sal)
    cnt=len(sal)
    avg=tot/cnt
    mx=max(sal)
    mn=min(sal)
    print("Total salary ",tot,"Count",cnt,"Average salary",avg,"Max sal ",mx,"Min sal",mn)
    
aggregatn(sal)


################################################################################################################
# Day 2

f=open("D:/mystuff/emp.txt")
h1=f.readline()
lines=f.readlines()
print(lines)
      

f2=open("D:/mystuff/emp.txt")
head=f2.readline()
lines=f2.readlines()
sal=[]
for v in lines:
    w=v.strip().split(',')
    sal.append(int(w[2]))
    print(w)


def aggregatn(x):
    tot=sum(sal)
    cnt=len(sal)
    avg=tot/cnt
    mx=max(sal)
    mn=min(sal)
    print("Total salary ",tot,"Count",cnt,"Average salary",avg,"Max sal ",mx,"Min sal",mn)
aggregatn(sal)



dictn={}
for v in lines:
    w=v.strip().split(',')
    sal=int(w[2])
    dno=int(w[-1])
    if dictn.get(dno)==None:
        dictn[dno]=sal
    else:
        dictn[dno]+=sal
print(dictn)
    
################################################################################################################
# Day 3


f=open("D:/mystuff/emp2.txt")
h=f.readline()
data=f.readlines()

"""
single grouping with single aggregation
sql:
    select sex , sum(sal) from emp2 group by sex;
"""

res1={}
for line in data:
    w=line.strip().split(",")
    sex=w[-2]
    sal=int(w[2])
    if res1.get(sex)==None:
        res1[sex]=sal
    else:
        res1[sex]+=sal
print(res1)

"""
multi grouping with single aggregation
sql:
    select dno,sex,sem(sal) from emp2 group by dno,sex;
    
"""        
 

res2={}
for line in data:
    w=line.strip().split(",")
    sex=w[-2]
    sal=int(w[2])
    dno=w[-1]
    mykey=(dno,sex)
    if res2.get(mykey)==None:
        res2[mykey]=sal
    else:
        res2[mykey]+=sal
print(res2)
for k,v in list(zip(res2.keys(),res2.values())):
    print("depatment :",k[0],"Sex :",k[1],"Sum :",v)
  
"""
single grouping with multiple aggregation
sql:
    select dno , sum(sal), count(*),avg(sal), max(sal),min(sal) from emp2 group by dno;

"""    
  

res3={}
for line in data:
    w=line.strip().split(",")
    sal=int(w[2])
    mykey=int(w[-1])
    if res3.get(mykey)==None:
        res3[mykey]=[sal]
    else:
        res3[mykey].append(sal)        
print(res3)  


finres={}
for k,v in list(zip(res3.keys(),res3.values())):
    tot=sum(v)
    cnt=len(v)
    avg=tot/cnt
    mx=max(v)
    mn=min(v)
    r=(tot,cnt,avg,mx,mn)
    finres[k]=r
print(finres)    
    
for k,v in list(zip(finres.keys(),finres.values())):
    print(k,v)


"""
multi grouping with multi aggregation
sql:
    select dno ,sex, sum(sal), count(*),avg(sal), max(sal),min(sal) from emp2 group by dno,sex;
    


"""


res4={}
for line in data:
    w=line.strip().split(",")
    mykey=(w[-1],w[-2])
    sal=int(w[2])
    if res4.get(mykey)==None:
        res4[mykey]=[sal]
    else:
        res4[mykey].append(sal)        
print(res4)  


fres={}
for k,v in list(zip(res4.keys(),res4.values())):
    tot=sum(v)
    cnt=len(v)
    avg=tot/cnt
    mx=max(v)
    mn=min(v)
    r=(tot,cnt,avg,mx,mn)
    fres[k]=r
    
for k,v in list(zip(fres.keys(),fres.values())):
    print(k,v)

o=["ravi","kavi","savi","tavi"]
'*'.join(o)


out=open("D:/mystuff/report.txt",'w')
hline='"dno","sex","tot","cnt","avg","mx","mn",\n'
out.write(hline)
for k,v in list(zip(fres.keys(),fres.values())):
    dno=k[0]
    sex=k[1]
    tot=str(v[0])
    cnt=str(v[1])
    avg=str(v[2])
    mx=str(v[-2])
    mn=str(v[-1])
    a=[dno,sex,tot,cnt,avg,mx,mn]
    newline=','.join(a)
    out.write(newline+"\n")
out.close()    


################################################################################################################
# Day 4


"""
How to perform Join with with file

Task:
    For each location salary budget
Sql:
select location , sum(sal) from emp2 e join dept d on e.dno=d.dno group by location:
 
"""
# Step-1   Transform master file(parent) as dictionary.

d=open("D:\mystuff\dept.txt")
h=d.readline()
dlines=d.readlines()
dinfo={}
for line in dlines:
    w=line.strip().split(',')
    dno=int(w[0])
    city=w[-1]
    dinfo[dno]=city
print(dinfo)    
    
# Step-2 Finding grouping aggregation.  
 
e=open("D:\mystuff\emp2.txt")
eh=e.readline()
elines=e.readlines()
res={}
for line in elines:
    w=line.strip().split(',')
    sal=int(w[2])
    dno=int(w[-1])
    city=dinfo.get(dno)
    if res.get(city)==None:
        res[city]=sal
    else:
        res[city]+=sal
        
print(res)    
 

    
# Denormalization

dinfo={}
for line in dlines:
    w=line.strip().split(',')
    dno=w[0]
    city=w[-1]
    dname=w[1]
    info=[dname,city]
    dinfo[dno]=info
print(dinfo)  


e=open("D:\mystuff\emp2.txt")
eh=e.readline()   
elines=e.readlines()
out=open("D:\mystuff\ed.txt","w")
for line in elines:
    dno=line.strip().split(',')[-1]
    d=dinfo[dno]
    dline=",".join(d)
    info=line.strip() + "," + dline + "\n"
    out.write(info)
out.close()







