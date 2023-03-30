
    while No>0:
        Digit = No%10
        No = No //10
        
    return Digit
    
def main():
    Ret = 0
    print("Entet the number :")
    value = int(input())
    
    Ret = DisplayDigits(value)
    print("Digits are :",Ret)
    
if __name__ == "__main__":
    main()
    