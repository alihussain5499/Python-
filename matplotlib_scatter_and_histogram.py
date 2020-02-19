import matplotlib.pyplot as mp

x=[1,2,3]
y=[4,5,6]
mp.scatter(x,y)
mp.show()

x=[1,2,3]
y=[4,5,6]
mp.scatter(x,y,s=50)
mp.show()


x=[1,2,3]
y=[4,5,6]
mp.scatter(x,y,s=50,c=['red','g','b'])
mp.show()

#histogram#
x=[1,2,3]
y=[10,20,30]
mp.hist(x)

x=[1,2,3]
y=[10,20,30]
mp.hist(y)

x=[1,2,3]
y=[10,20,30]
mp.hist(x)
mp.hist(y)

import numpy as np
data=np.random.normal(2.0,3.0,1000)
mp.hist(data,histtype="step")
mp.show()


data=np.random.normal(2.0,3.0,1000)
mp.hist(data,histtype="bar")
mp.show()


data=np.random.normal(2.0,3.0,1000)
mp.hist(data,histtype="bar",orientation='vertical',stacked='true')
mp.show()


data=np.random.normal(2.0,3.0,1000)
mp.hist(data,histtype="bar",orientation='vertical',stacked='true',log='false')
mp.grid()
mp.show()


data=np.random.normal(2.0,3.0,1000)
mp.hist(data,histtype="bar",orientation='horizontal',stacked='true',log='true')
mp.show()


data=np.random.normal(2.0,3.0,1000)
mp.hist(data,bins='auto',histtype="bar",orientation='horizontal',stacked='true',log='true')
mp.show()


data=np.random.normal(2.0,3.0,1000)
mp.hist(data,histtype="bar",orientation='vertical',stacked='true',log='true')
mp.grid()
mp.show()





