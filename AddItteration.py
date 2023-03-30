
def iteration(value):
    result = 0

    for i in range(0,value):
        result = result + i
    return result

def main():
    print("Enter the number :")
    no = int(input())
    
    Ret = iteration(no)
    print("Addition of first numbers are :",Ret)

if __name__ == "__main__":
    main()