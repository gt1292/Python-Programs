def Factors(Value):
    for i in range(1,int(Value/2)+1):   # this is main efficient part
        if Value % i == 0:
            print(i, end=" ")
            i = i+1


def main():
    print("Enter the number :")
    no = int(input())

    Factors(no)


if __name__ == "__main__":
    main()
