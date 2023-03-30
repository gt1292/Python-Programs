# Program to count number of factors

fact = list()
def CntFactor(value):
    for i in range(1,value):
        if value % i == 0:
            fact.append(i)
    return len(fact) 
           
            
def main():
    print("Enter the number :")
    no = int(input())
    
    Ret = CntFactor(no)
    print("Total number of factors are :",Ret)

if __name__ == "__main__":
    main()
    
"""    
#Program to count non factors

fact = list()
def CntNonFact(value):
    for i in range(1,value):
        if value % i != 0:
            fact.append(i)
    return len(fact)
    
def main():
    print("Enter the number :")
    no = int(input())
    
    ret = CntNonFact(no)
    print("Total number of non factors :",ret)
    
if __name__ == "__main__":
    main()
    
"""
