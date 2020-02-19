class student:
    def __init__(self):
          print("hello")
     

s=student()         

class student:
    def __init__(self):
          print("hello")
     
    def __init__(self,a):
         print("hi",a)
         
s=student("")
s=student("10")         

class student:
    
    def __init__(self):
          print("hello")
     
    def sample(self,a,b):
        global c
        c=a+b
        return(c)

class  student_1(student):
    def input(self):
        global a,b
        a=int(input("enter a value   "))
        b=int(input("enter b value   "))
        return
s1=student_1()
s1.input()
s1.sample(a,b)
