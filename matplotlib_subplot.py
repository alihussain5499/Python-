import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axis3d

mp.subplot()

mp.subplot(122)
mp.show()

mp.subplot(882)
mp.show()

mp.subplot(122)
mp.plot(x,marker="*",linestyle=":",label="IES")
mp.legend()
mp.show()

mp.subplot(122)
mp.plot(x,marker="^",linestyle=":",label="IES")
mp.legend()
mp.show()

mp.subplot(122)
mp.plot(y,marker="^",linestyle=":",label="IES_school")
mp.legend()
mp.show()

x=[1,2,3]
y=[1,2,3]
fig=mp.figure(1)
fig.add_subplot(175,facecolor="red")
mp.plot(x)
mp.show()
x=[1,2,3]
y=[1,2,3]
fig1=mp.figure(2)
fig1.add_subplot(175,facecolor="green")
mp.plot(y)
mp.grid()
mp.show()


x=[1,2,3]
y=[1,2,3]
fig=mp.figure(1)
fig.add_subplot(175,facecolor="c")
mp.plot(x)
mp.show()
x=[1,2,3]
y=[1,2,3]
fig1=mp.figure(2)
fig1.add_subplot(175,facecolor="M")
mp.plot(y)
mp.show()



























