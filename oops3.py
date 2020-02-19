class Demo:
    def __init__(self):
        print("hello")
    def __del__(self):
        print("deleted")

d=Demo()
del d 

class Demo:
   a=12
  
Demo.a   

class Demo:
    def sample(self):
        print("hello")
    def sample(self,a):
        print(a)
 
d=Demo()
d.sample(10) 


class Demo:
    def sample():
        print("hello")  
 
Demo.sample()       