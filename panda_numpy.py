import pandas as pd
import numpy as  np
data=pd.read_csv("IRIS.csv")
data.head
data.head()
x=data.iloc[:,:4]
y=data.iloc[:,4]


from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/2)
x_train

from sklearn.preprocessing import  StandardScaler
scaler=StandardScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)
x_train

from sklearn.neighbors import KNeighborsClassifier #connect to knn algo#
classifier=KNeighborsClassifier()#object to neighbor#
classifier.fit(x_train,y_train)

y_predict=classifier.predict(x_train)
y_predict

import matplotlib.pyplot  as mp
error=[]
for  i in range(1,20):
    k=KNeighborsClassifier(n_neighbors=i)
    k.fit(x_train,y_train)
    y_prediction=k.predict(x_train)
    error.append(np.mean(y_prediction!=y_train))
    
mp.plot(range(1,20),error,marker="*",color="red")
mp.title("Error rate calculation ")
mp.show()
    