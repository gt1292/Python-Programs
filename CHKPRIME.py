
class Value:
    def __init__(self, Data):
        self.No = Data

    def ChkPrime(self):
        i = 0
        Flag = True
        for i in range(2, int(self.No / 2)+1):
            if (self.No % i == 0):
                Flag == False
                break
            
        return Flag


def main():
    print("Enter the number :")
    A = int(input())

    obj = Value(A)

    Ret = obj.ChkPrime()
    if (Ret == True):
        print("{} is a prime number".format(A))
    else:
        print("{} is not a prime number".format(A))


if __name__ == "__main__":
    main()
