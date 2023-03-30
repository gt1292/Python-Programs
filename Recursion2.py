# Factorial By recursion
def Fact(No):
   
    if(No <= 0):
        return 1
    else:
        return (No * Fact(No - 1))

Ret = Fact(4)

print("Result is :",Ret)

# Recursive program to add itteration
"""
def Add(No):
   
    if(No <= 0):
        return 0
    else:
        return (No + Add(No - 1))

Ret = Add(4)

print("Result is :",Ret)
"""


# Addition of itteration program
"""
def Add(No):
    Ans = 0
    while(No >= 0):
        Ans = Ans+No
        No = No - 1
    return Ans

Ret = Add(4)

print("Result is :",Ret)
"""

# Recursion to reverse number
"""
def Display(No):
   
    if(No > 0):
        No = No - 1 
        Display(No) # Recursive Call
        print(No)
        
Display(4)
"""