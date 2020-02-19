import matplotlib.pyplot as mp

from mpl_toolkits.mplot3d import axis3d
mp.subplot(projection='3d')
mp.show()


x=[1,2,3]
y=[1,2,3]
fig=mp.figure(1)
fig.add_subplot(175,facecolor="c",projection='3d')
mp.plot(x,y)
mp.show()


