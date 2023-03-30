import multiprocessing
import os

def Square(No):
    print("PID of worker process is {} for the input {}".format(os.getpid(),No))
    return (No*No)

def main():
    print("Process id of our application is :",os.getpid())
    data = [1,2,3,4,5]
    Result = []
    
    pool = multiprocessing.Pool()
    Result = pool.map(Square , data)
    
    print("Result after the square is :",Result)

if __name__ == "__main__":
    main()
    