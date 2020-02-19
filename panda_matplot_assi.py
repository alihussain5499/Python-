#KMeans algo#
import pandas as pd
data=pd.read_csv("Position_Salaries.csv")
data.head()
x=data.iloc[:,[1,2]].values
from sklearn.cluster import KMeans
km=KMeans(n_clusters=5,init="k-means++",random_state=0)
km.fit(x)
y_pred=km.predict(x)
y_pred
import matplotlib.pyplot as plt
plt.scatter(x[[y_pred==1,0]],x[[y_pred==1,1]],c="red",label="Cluster_1")
plt.scatter(x[[y_pred==2,0]],x[[y_pred==2,1]],c="blue",label="Cluster_2")
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],s=400,c="green")
plt.title("Position_Salary")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.legend()
plt.show()


#Polynomial Regression#
x=data.iloc[:,1:2].values
y=data.iloc[:,2:3].values

from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=3)
x_poly=poly_reg.fit_transform(x)


from sklearn.linear_model import LinearRegression
slr=LinearRegression()
slr.fit(x_poly,y)
import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.plot(x,slr.predict(x_poly),color='g')
plt.show()


#Linear Regression#

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x,y)
y_predict=lr.predict(x)

import matplotlib.pyplot as plt
plt.scatter(x,y,color='g')
plt.plot(x,y_predict)
print(lr.predict(9))
plt.show()




import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axis3d


mp.subplot(122)
mp.plot(y,marker="^",linestyle=":",label="Salary")
mp.legend()
mp.show()

x=[10000,20000,30000,40000,500000,60000,700000,8000,9000,1000000000]
y=[1,2,3,4,5,6,7,8,9,10]
fig=mp.figure(1)
fig.add_subplot(175,facecolor="red")
mp.plot(x)
mp.show()



