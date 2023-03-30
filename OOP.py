# Accccept 2 number and perform addition and substraction of it

# kay karaych ahe ?   -> behaviour (function)
# te karayla kay lagnar ahe -> Characteristics
# class = characteristics + behaviour
# class = data + function

class Arithmatic:
    def __init__(self, A, B):
        self.no1 = A
        self.no2 = B

    def Add(self):
        return self.no1+self.no2

    def Sub(self):
        return self.no1-self.no2


def main():
    print("Enter first number :")
    no1 = int(input())
    print("Enter second number :")
    no2 = int(input())

    obj = Arithmatic(no1,no2)
    
    Ans = obj.Add()
    print("Addition is :",Ans)
    
    Ans = obj.Sub()
    print("Substraction is :",Ans)

if __name__ == "__main__":
    main()
