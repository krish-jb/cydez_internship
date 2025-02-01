# Write a Python program to check if a given value is a method of a user-defined class. Use types.MethodType()
import types

class Methods:
    def meth1(self):
        pass
    
    def meth2(self):
        pass
    
    def meth3(self):
        pass
      
      
def meth4():
    pass

  
obj = Methods()
func1 = obj.meth1
func2 = meth4

print(isinstance(func1, types.MethodType))
print(isinstance(func2, types.MethodType))