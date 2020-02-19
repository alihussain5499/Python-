import pandas as pd
data=pd.read_csv("C://Users//acer//Desktop//exp.csv")
data
x=data.iloc[:,0:1].values#it gives values in array#
#deviding the data#
y=data.iloc[:,1:].values

#dividing training and testing data#
from sklearn.cross_validation import train_test_split
train_test_split(x,y,train_size=1/7)

from sklearn.cross_validation import train_test_split
train_test_split(x,y,train_size=0.5)


from sklearn.cross_validation import train_test_split
train_test_split(x,y,train_size=0.7)


from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7)

#linear regration#
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x,y)
y_predict=lr.predict(x)

import matplotlib.pyplot as plt
plt.scatter(x,y,color='r')
plt.show()

plt.scatter(x,y,color='r')
plt.plot(x,y_predict)
plt.show()


plt.scatter(x,y,color='r')
plt.plot(x,y_predict)
print(lr.predict(9))
plt.show()














