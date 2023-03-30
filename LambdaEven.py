

def ChkEvenX(No):
    return (No % 2 == 0)


ChkEven = lambda No : No % 2 == 0 # Lambda Function


Ret = ChkEven(12)

if (Ret == True):
    print("Its even")
else:
    print("Its Odd")


