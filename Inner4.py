# This is Decorator Program Swapping in it

def Substraction(No1,No2):
    Ans = 0
    Ans = No1-No2
    return Ans
    
def Decorated_Function(Function_Name):
    def Inner(A,B):
        if(A<B):
            A,B = B,A
        return Function_Name(A,B)
    return Inner

def main():
    value1 = int(input("Enter First Number : "))
    value2 = int(input("Enter second Number : "))
    
    New_Function = Decorated_Function(Substraction)
    print(New_Function(value1,value2))
    
if __name__ == "__main__":
    main()