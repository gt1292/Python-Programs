class Value:
    def __init__(self, Data):
        self.No = Data

    def SumFactor(self):
        sum = 0

        for i in range(1,int(self.No/2 + 1)):
            if (self.No % i == 0):
                sum = sum + i
        return sum

    def ChkPerfect(self):
        Ans = self.SumFactor()
        if (self.No == Ans):
            return True
        else:
            return False


def main():
    print("Enter the number :")
    A = int(input())

    obj = Value(A)

    Output = obj.SumFactor()
    print("Summation of factor is :", Output)

    Ret = obj.ChkPerfect()
    if (Ret == True):
        print("{} is a perfect number".format(A))
    else:
        print("{} is not a perfect number".format(A))


if __name__ == "__main__":
    main()
