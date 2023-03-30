from functools import reduce


ChkEven = lambda No: No % 2 == 0
Doubles = lambda No: No*2
Sum = lambda A, B: A+B

###################################################


def reduce(Helper_Function, Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans, no)

    return Ans

####################################################


def filter(Helper_Function, Data):
    result = []
    for No in Data:
        if (Helper_Function(No) == True):
            result.append(No)
    return result

###################################################


def map(Helper_Function, Data):
    result = []
    for No in Data:
        value = Helper_Function(No)
        result.append(value)
    return result

###################################################


def main():
    print("Demonstration of Filter Map Reduce")

    print("Enter number of Elements that you want :")
    iSize = int(input())

    Data_Input = []
    print("Enter the data :")

    for iCnt in range(0, iSize, 1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is :", Data_Input)

    Data_Filter = list(filter(ChkEven, Data_Input))
    print("Data after filter is :", Data_Filter)

    Data_map = map(Doubles, Data_Filter)
    print("Data after map :", Data_map)

    Output = reduce(Sum, Data_map)
    print("Data After Reduce :", Output)


if __name__ == "__main__":
    main()
