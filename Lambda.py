# Normal functions / nanmed functions
def Add(No1, No2):
    return No1 + No2

# Lambda Functions / Un-named Function
# lambda parameter : body


AddFunction= lambda A, B: A+B


Ans1 = Add(10, 11)
Ans2 = AddFunction(10, 11)

print("Addition using normal function :", Ans1)
print("Addition using lambda function :", Ans1)

print("Type of lambda function is :",type(AddFunction))

