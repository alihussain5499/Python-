import pandas as pd
data=pd.read_csv("C://Users//acer//Desktop//exp1.csv")
data
x=data.iloc[:,0:1].values
y=data.iloc[:,1:].values


print(x)
print(y)

import matplotlib.pyplot as plt
plt.scatter(x,y,color='g')
plt.show()

#a=(sum(y))*(sum(x**2))-((sum(x))*(sum(x*y)))/8*(sum(x**2))-(sum(x))**2#
#b=8*(sum(x*y))-(sum(x))*sum(y)/8*(sum(x**2))-(sum(x**2))#
#print(a,b)#



a_1=sum(x)
a_2=sum(y)
a_3=sum(x*y)
a_4=sum(x**2)
print(a_1,a_2,a_3,a_4)

ar=(a_2*a_4)-(a_1*a_3)
ar

al=(8*a_2)-(a_1**2)
al

a=ar/al
a

br=(8*a_3)-(a_1*a_2)
br

bn=(8*a_4)-(a_4)
bn

b=br/bn
b

y=a+(b*x)
y



