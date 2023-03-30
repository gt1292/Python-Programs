# Area of circle

def Area(Radius, PI = 3.14):
    Result = PI * Radius * Radius
    return Result

def main():
    Rvalue = 10.5
    PIvalue = 3.14

    # Positional argument
    ans = Area(Rvalue, PIvalue)     # Default Argument
    print("Area of circle is :", ans)
    
    # Positional argument and second is default
    ans = Area(10.5)     # Default with positional
    print("Area of circle is :", ans)
    
    # keyword arguments
    ans = Area(PI = 7.10 , Radius=10.5)   # Default argument with keyword
    print("Area of circle is :", ans)

if __name__ == "__main__":
    main()
