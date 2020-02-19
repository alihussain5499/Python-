import matplotlib.pyplot as mp
import pandas as pd

import numpy as np
x=[1,2,3]
y=[4,5,6]
mp.bar(x,y)
mp.show()

x=[1,2,3]
y=len(x)
mp.bar(x,y)
mp.show()

from scipy import misc
fg=misc.face()
misc.imsave("sap.png",fg)
mp.imshow(fg)
mp.show()


fg=misc.imread("F://DCIM//Camera//a.jpg")
mp.imshow(fg,origin=0)
mp.show()


fg=misc.imread("F://DCIM//Camera//c.jpg")
mp.imshow(fg)
mp.show()



fg=misc.imread("F://DCIM//Camera//n.jpg")
mp.imshow(fg)
mp.show()

fg=misc.imread("F://DCIM//Camera//g.jpg")
fg.partition(1)
mp.imshow(fg,origin=0)
mp.grid()
mp.show()

from scipy import misc,ndimage

fg=misc.imread("C://Users//acer//Desktop//v.jpg")
ndimage.gaussian_filter(fg,sigma=1000)
mp.imshow(fg)
mp.show()

#diplay excel fine in graph #
df=pd.read_csv("data.csv")
df
mp.hist(df)

mp.hist(df[['EST','event']][df.event=='rain'])

x=([df.event=='rain'])
y=([df.EST=='rain'])
mp.scatter(x,y)
mp.show()

a=df[['EST']][df.event=="rain"]
a
mp.plot(a,marker="*",linestyle="--",color="black",markersize=9,linewidth=1)
mp.xlabel("event")
mp.ylabel("EST")
mp.legend()
mp.show()

