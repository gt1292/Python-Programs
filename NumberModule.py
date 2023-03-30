def DisplayFactors(Value):
    i = 1  # explicitely to create variable i
    while (i <= int(Value/2)):   # this is main efficient part
        if Value % i == 0:
            print(i)
        i = i + 1


def Factors(Value):
    for i in range(1, int(Value/2)+1):   # this is main efficient part
        if Value % i == 0:
            print(i, end=" ")
            i = i + 1

def Addition(value1 , value2):
    Ans = value1 + value2
    return Ans
