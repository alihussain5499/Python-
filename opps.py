#oops#
class student:
    a=12
    def sample(self):
      a=15
      print(a)
      return
  
s=student()
s.sample()    

class student:
    a=20        # public variable
    def sample(self):
      print(self.a)
      return 
  
s=student()
s.sample()    


s=student()
print (s.a)    

s=student()
s.sample()    

class student:
    __a=20        #private variable
    _a=40       #protected variable
    def __sample(self):
      print(self.a)
      return 
 
s=student()
s.sample()
