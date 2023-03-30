

class Numbers:
    def __init__(self):
        self.size = 0
        self.Arr = list()
        self.Accept()

    def Accept(self):
        print("Enter the elements you want :")
        self.size = int(input())

        print("Entet the elements :")
        Value = 0
        for i in range(0, self.size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elements from list are :")
        for i in range(0, self.size):
            print(self.Arr[i])

    def Summation(self):
        Sum = 0
        for i in range(0, self.size):
            Sum = Sum + self.Arr[i]
        return Sum

    def Average(self):
        Sum = 0
        for i in range(0, self.size):
            Sum = Sum + self.Arr[i]
        return (Sum/self.size)

    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0, self.size):
            if (self.Arr[i] > Max):
                Max = self.Arr[i]
        return Max

    def Minimum(self):
        Min = self.Arr[0]
        for i in range(0, self.size):
            if (self.Arr[i] < Min):
                Min = self.Arr[i]
        return Min


def main():
    obj = Numbers()
    obj.Display()

    Output = obj.Summation()
    print("Summation of all elements is:", Output)

    Output = obj.Average()
    print("Average of all elements is:", Output)

    Output = obj.Maximum()
    print("Largest elements is:", Output)
    
    Output = obj.Minimum()
    print("Smallest elements is:", Output)


if __name__ == "__main__":
    main()
