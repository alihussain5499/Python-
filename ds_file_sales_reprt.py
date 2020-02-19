# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:39:05 2019

@author: ali hussain
"""

"""
Task1.
Generate Monthly sales report.
Task2.
Generate Quarterly sales report.
Task3.
comporison of current quarter sales with previous
quarter sales [ how much percentage increased or
decreased ]
"""

# task1 : monthly sales report.


f = open("D:/mystuff/sales.txt")
h = f.readline()
lines = f.readlines()
mrep = {}
for line in lines:
    
    w = line.strip().split(",")
    m = int(w[0].split("/")[0])
    amt = int(w[1])
    if mrep.get(m)==None:
        mrep[m]=amt
    else:
        mrep[m]+=amt
print(mrep)


# task2:

qrep={}
for m in mrep:
    amt = mrep[m]
    q=4
    if m<4:
        q=1
    elif m<7:
        q=2
    elif m<10:
        q=3
    if qrep.get(q)==None:
        qrep[q]=amt
    else:
        qrep[q]+=amt
for q in qrep:
    print(q, qrep[q])

#Task 3

q1 = [(q,qrep[q]) for q in qrep]
print(q1)


q2 = q1
results =[]
for x in q1:
    cq = x[0]
    cs = x[1]
    for y in q2:
        pq= y[0]
        ps= y[1]
        if (cq-pq)==1:
            results.append((cq,pq,cs,ps,(cs-ps)/ps * 100))
for v in results:
    print(v)
