import sys

print(sys.getrecursionlimit())

def Display(No):
    
    if(No>0):
        print("Hello")
        No = No - 1
        Display(No)  #tail recursion
        
Display(4)

"""
def Display(No):
    cnt = 0
    while(cnt<No):
        print("Hello")
        cnt = cnt+1
        
Display(4)
"""