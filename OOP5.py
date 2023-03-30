class Value:
    def __init__(self, Data):
        self.No = Data

    def ChkPrime(self):
        i = 0
        for i in range(2, int(self.no / 2)+1):
            if (self.No % i == 0):
                break
            
        if (i == int(self.No/2)):
            return True
        else:
            return False


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
