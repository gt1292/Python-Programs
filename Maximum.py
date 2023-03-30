#Application to find out maximum number

def Maximum(no1,no2):
    if no1 > no2:
        return no1
    else:
        return no2

def main():
    print("Enter First Number :")
    value1 = input()
    
    print("Enter Second number :")
    value2 = input()
    
    Max = Maximum(int(value1),int(value2))
    
    print("Maximum number is :",Max)
  
if __name__ == "__main__":
    main()
    