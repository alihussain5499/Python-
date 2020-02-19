d={100:"ben",101:"10"}
d

d={101:"ben",100:"10"}
d

d1={101:" ",102:" "}
d1


d3={"abc":100,"abc":101}
d3

d4={}
d4
d4[1]="krishna"
d4[2]="venkat"
d4
print(d4[2])

del(d4[2])
d4

del(d4)
d4

len((d))
d.pop(100)

d1={100:"v",101:"u"}
d2={103:"w",104:"n"}
d1.update(d2)
d1

d1={100:"v",101:"u"}
d2={}
d2=d1.copy()
d2

d2.get(100)
print(d2.get(101))

d4.fromkeys("krishna")

d.popitem()

d.setdefault(100)
d

name="krishna"
for i in "aeiou":
    name=name.replace(i,"")
print(name)    

name="AAAAccccggggyutir"
count=0
for i in range(0,len(name)):
    for j in range(i+1,len(name)):
        if(name[i]==name[j]):
            count=count+1
print(count)            




