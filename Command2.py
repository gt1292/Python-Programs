from sys import *

def Addition(A,B):
    Ans = 0
    Ans = A+B
    return Ans

def main():
    print("Welcome to :",argv[0])
    
    if(len(argv) == 2):
        if(argv[1] == "--U"):
            print("use the application as : ")
            print("Python Name_of_Application First_number Second_number")
            exit()
            
        if(argv[1] == "--H"):
            print("Help : this application is used to perform addition of two numbers")
            exit()
            
            
    if((len(argv) != 3)):
        print("Invalid number of arguments")
        exit()
        
    Ret = Addition(int(argv[1]), int(argv[2]))
    print("Addition is :",Ret)
    
    print("Thank you for using Marvellous Infosystem")
    
    
if __name__ == "__main__":
    main()