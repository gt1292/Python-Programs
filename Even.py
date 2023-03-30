def ChkEven(value):
    if((value % 2) == 0):
        return True
    else:
        return False
    
def main():
    print("Enter the number :")
    no = int(input())
    
    Bret = ChkEven(no)
    if(Bret == True):
        print(no,"is Even")
    else:
        print(no,"Odd number")

if __name__ == "__main__":
    main()
