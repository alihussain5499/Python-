import pandas as pd
data=pd.read_csv("Customers.csv")
data.head()

x=data.iloc[:,[3,4]].values

from sklearn.cluster import KMeans
km=KMeans(n_clusters=5,init="k-means++",random_state=0)
km.fit(x)
y_pred=km.predict(x)
y_pred

import matplotlib.pyplot as plt
plt.scatter(x[[y_pred==0,0]],x[[y_pred==0,1]],c="red",label="Cluster_1")
plt.scatter(x[[y_pred==1,0]],x[[y_pred==1,1]],c="blue",label="Cluster_2")
plt.scatter(x[[y_pred==2,0]],x[[y_pred==2,1]],c="cyan",label="Cluster_3")
plt.scatter(x[[y_pred==3,0]],x[[y_pred==3,1]],c="yellow",label="Cluster_4")
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],s=300,c="black")
plt.title("G V K Mall")
plt.xlabel("Annual_Income")
plt.ylabel("Spending_Score")
plt.legend()
plt.show()


elb=[]
for i in range(1,11):
    k=KMeans(n_clusters=i,random_state=0)
    k.fit(x)
    y_predict=k.predict(x)
    elb.append(k.inertia_)
    
    
plt.plot(range(1,11),elb)
plt.show()   