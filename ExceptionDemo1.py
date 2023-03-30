# Exception Handling Program

def main():
    try:
        print("Enter First Number :")
        No1 = int(input())
        
        print("Enter Second Number :")
        No2 = int(input())
    
        Ans = No1/No2
        print("Division is :",Ans)
    
    except ZeroDivisionError:
        print("inside zero division error")
        
    except NameError:
        print("Inside name error")
        
    except ValueError:
        print("Inside value error")
        
    finally:
        print("Inside finally block")
    
if __name__ == "__main__":
    main()
    