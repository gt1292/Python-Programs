#Program to find factor of number

def Factor(value):
    
    for i in range(1,value):
        if value % i == 0:
            print(i)

def main():
    print("Enter the number :")
    no = int(input())
    
    Factor(no)

if __name__ == "__main__":
    main()
    

"""
# program to find non factors

def Factor(value):
    
    for i in range(1,value):
        if value % i != 0:
            print(i)

def main():
    print("Enter the number :")
    no = int(input())
    
    Factor(no)

if __name__ == "__main__":
    main()
"""