# To take input from user in format of list

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


if __name__ == "__main__":
    main()
