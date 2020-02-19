import pandas as pd
pd.Series()
#by using list create array#
data=[1,2,3]
pd.Series(data)

pd.Series(data,index=["id","marks","percent"])

#by using tuple create array#
songs=("i am feeling","i am lucky in the world")
artist=("ali","ah")
s=pd.Series(data=songs,index=artist)
s
s.values

s=pd.Series(data=songs,index=artist,dtype=str)
s.values
#by using dictionary create array#
n={'ali':0,'marks':10}
dic=pd.Series(data=n)
dic

dic=pd.Series(data=n,index=["ali","abs"]) #it takes null values #
dic

#by using numpy creating array#
import numpy as np
data1=np.array([1,2,3])
data1
p=pd.Series(data=data1)
p

p=pd.Series(data=data1,index=([10,11,12]))
p
p[10]


#by using list create array #
p1=[1,2,3]
p2=pd.Series(data=p1)
p2
p2[0]

#slicing #
p2[1:]
p2[:1]
p2[:4]

d1={"Name":["Ali","abc","vds"],"Marks":[10,11,12]}
d1
pd.DataFrame(data=d1,index=["rank1","rank2","rank3"])

#2d array list with dictionary#

l1=[{"a":1,"b":2},{"a":2,"b":3,"c":5}]
pd.DataFrame(data=l1)
pd.DataFrame(data=l1,index=["id","rno"])

#2d array  dictionary with list#
d2={"one":pd.Series(["ali","sap"],index=[1,2]),
    "two":pd.Series([12],index=[1])}
d2["three"]=pd.Series([12,14],index=[1,2])
dat=pd.DataFrame(data=d2)

dat['four']=dat['two']+dat['three']
dat

del  dat['four']
dat

p=pd.Series(["ali","vak"],index=['a','b'])
p1=pd.DataFrame(data=p)
p1
p1.loc['b']

dat.iloc[1]
dat.iloc[0]

dat.describe()

dat.describe(include="all")

a=pd.Series([1,2,3],index=[1,2,3])
b=pd.Series([1,2],index=[1,2])
c=pd.DataFrame(data=[a,b])
d=pd.Series([5,6],index=[4,5])


c.reindex(d)

a1=pd.DataFrame(np.random.randn(10,3))
a1

a1=pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
a1

a1=pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
a2=pd.DataFrame(np.random.randn(2,4),columns=['col1','col2','col3','col4'])


var=a1.reindex_like(a2)
var.fillna(2)

a1=pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
a2=pd.DataFrame(np.random.randn(2,2),columns=['col1','col2'])

a1.reindex_like(a2)



#excel file featching from system file in C:\Users\acer\.spyder-py3 #
df=pd.read_csv("data.csv")
df

df['EST']
df['Temperaturee']
df[df.Temperaturee>=24]
df[['EST','Temperaturee']]
df.head()
df.tail()

a=df[['EST','event']]
a[a.event=='rain']

df[df.event=='rain']
[df.event=='rain']

a=df[['EST','event']][df.event=='rain']


df.to_csv("a.csv")
ab=pd.read_csv("a.csv")
ab

ab=pd.read_csv("C://Users//acer//.spyder-py3//a.csv")
ab

a=[1,2,3]
b=[2,3,4]

zip?

c=list(zip(a,b))
c





