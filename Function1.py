# Functions which accept nothing and return nothing
def Demo():
    print("inside demo")

# Function accept one parameter and return nothing
def Demo1(No):
    print("Inside Demo1 with argument",No)
    
# Function accepts one parameter and return one parameter
def Demo2(No):
    print("Inside demo2 with argument",No)
    return No +2

# Function accepts two parameter and return one parameter
def Demo3(No1,No2):
    print("Inside Demo3")
    Add = No1+No2
    return Add


# Function accepts two parameter and return two parameter
def Demo4(No1,No2):
    print("Inside Demo4")
    Add = No1 + No2
    Sub = No1 - No2
    return Add,Sub

def main():
    Demo()
    Demo1("Hello")
    Ans = Demo2(10)
    print("Return Value of demo2",Ans)
    
    Ans = Demo3(11,21)
    print("Return Value Addition is :",Ans)
    
    Ans1,Ans2 = Demo4(11,21)
    print("Return Value Addition is :",Ans1)
    print("Return Value Subsctraction is :",Ans2)
    
if __name__ == "__main__":
    main()
    
