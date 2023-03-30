#import NumberModule 
#from numbers import *
from NumberModule import DisplayFactors #efficient specific import

def main():
    print("Enter the number :")
    no = int(input())

    DisplayFactors(no)

if __name__ == "__main__":
    main()

