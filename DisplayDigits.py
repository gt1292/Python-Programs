

def DisplayDigits(No):
    while No>0:
        Digit = No%10
        No = No //10
        print(Digit)
        
    
    
def main():
    Ret = 0
    print("Entet the number :")
    value = int(input())
    
    DisplayDigits(value)
    
    
if __name__ == "__main__":
    main()
    