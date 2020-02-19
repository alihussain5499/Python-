import pandas as pd
data=pd.read_csv("C://Users//acer//Desktop//exp.csv")
data
x=data.iloc[:,0:1].values
#deviding the data#
y=data.iloc[:,1:].values




#polynomial regration#

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





