import matplotlib.pyplot as mp

import numpy as np
check=np.zeros((9,9))
check[::2,1::2]=1
check[1::2,::2]=1
import matplotlib.pyplot as plt
plt.imshow(check,cmap="gray",interpolation='nearest')
plt.show()


x=[1,2,3]
mp.pie(x)
mp.show()


x=[1,2,3]
color=["yellow","orange",'pink']
mp.pie(x,colors=color)
mp.show()


x=[1,2,3]
color=["yellowgreen","lightskyblue","orange"]
label=["samsumg","sony","vivo"]
mp.pie(x,colors=color,labels=label)
mp.legend()
mp.show()


x=[1,2,3]
color=["yellowgreen","lightskyblue","orange"]
label=["samsumg","sony","vivo"]
mp.pie(x,colors=color,labels=label)
mp.legend()
mp.axis("equal")
mp.show()


x=[1,2,3]
color=["yellowgreen","lightskyblue","orange"]
label=["samsumg","sony","vivo"]
mp.pie(x,colors=color,labels=label,shadow='true')
mp.legend(loc="upper left")
mp.axis("equal")
mp.show()


x=[1,2,3]
color=["yellowgreen","lightskyblue","orange"]
label=["samsumg","sony","vivo"]
mp.pie(x,colors=color,labels=label,shadow='true',startangle=90)
mp.legend(loc="upper left")
mp.axis("equal")
mp.show()


















