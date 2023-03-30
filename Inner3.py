
def Outer():
    print("Inside Outer")
    
    def Inner():
        print("Inside inner")
        
    print(id(Inner))
    return Inner

Ret = Outer()
print(type(Ret))
print(id(Ret))
Ret()