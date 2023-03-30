def add(A,B):
    return A+B

def sub(A,B):
    return A-B

def main():
    print("Enter first number :")
    no1 = int(input())
    print("Enter second number :")
    no2 = int(input())
    
    ans = add(no1,no2)
    print("Addition is :",ans)
    
    ans = sub(no1,no2)
    print("Substraction is :",ans)
    
    
if __name__ == "__main__":
    main()