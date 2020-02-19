# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:08:48 2019

@author: ali hussain
"""

f=open("D:/mystuff/matrimony.txt")
h=f.readline()
lines=f.readlines()
print(len(lines))

males=[]
fems=[]
for line in lines:   
    w=line.strip().split(",")
    sex= w [2]
    name=w[1]
    age=int(w[3])
    sal=int(w[-2])
    city=w[-1]
    info = (name,sex,age,sal,city)
    if sex=="m":
        males.append(info)
    else:
        fems.append(info)
print(males)
print("_"*60)
print(fems)

# task : for each male, generate possible female list based on given
# criteria.
#male age > fem age
#age gap <=4
# male income > fem income
#matches = []

outfile = open("D:/mystuff/matriMatches.txt","w")
hd = [ '"mname"','"msex"','"mage"','"minc"','"mcity"',
'"fname"','"fsex"','"fage"','"finc"','"fcity"',"\n"]
outfile.write(",".join(hd))
for m in males:
    mage=m[2]
    minc=m[-2]
    for f in fems:
        finc=f[-2]
        fage=f[2]
        if mage>fage and minc>finc and (mage-fage)<=4:
            l = list(m)+list(f)
            ln = [str(v) for v in l]
            outfile.write(",".join(ln)+"\n")
outfile.close()