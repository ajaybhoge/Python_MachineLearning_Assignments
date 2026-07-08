from functools import reduce
Ret = lambda x,y:x*y
def main():
    Value= int(input("Enter the Number : "))
    Data = []

    for i in range(1, Value+1):
        Values =int(input("Enter the Number : "))
        Data.append(Values)

    print(Data)
    Result = reduce(Ret,Data)

    print(Result)
    

if __name__ =="__main__":
    main()