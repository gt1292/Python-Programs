print("Application to demonstrate Industrial Programming")

#Addition Program 6 creating new function for addition Best Program 
def Addition(value1 , value2):
    Ans = value1 + value2
    return Ans

def main():
    print("Enter First number :")
    no1 = int(input())
    print("Enter Second Number :")
    no2 = int(input())
    
    Sum = Addition(no1,no2)
    print("Addition is :",Sum)

if __name__ == "__main__":
    main()


"""
#  Addition Program 5 user interactive Program 
def main():
    print("Enter First number :")
    no1 = input()
    print("Enter Second Number :")
    no2 = input()
    
    Ans = int(no1) + int(no2)   #Typeconversion temprory
    print("Addition is :",Ans)

if __name__ == "__main__":
    main()
"""


#Addition Program 4 one of Better Approach
#def main():
#    no1 =10
#    no2 =11
#    Ans = no1 + no2
#    print("Addition is :",Ans)
    
#if __name__ == "__main__":
#    main()


#Addition Program 3
#def main():
#    no1 =10
#    no2 =11
#    Ans = no1 + no2
#    print("Addition is :",Ans) 
#main()


#Addtion Program 2
#no1 = 10 
#no2 = 11
#ans = no1+no2
#print("Addition is :",ans)


#Addition Program 1
#print("Addition is :",11+10)