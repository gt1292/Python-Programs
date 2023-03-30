
def Hello():
    print("Inside hello")
    
def Fun():
    print("Inside Fun")

def Demo(FPTR):
    print("Inside Demo")
    FPTR()

Demo(Hello)
Demo(Fun)