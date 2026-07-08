Ret = lambda x: x if (x % 5 == 0) and (x % 3 == 0) else False

def main():
    Value= int(input("Enter the Number : "))
    Data = []

    for i in range(1, Value+1):
        Values =int(input("Enter the Number : "))
        Data.append(Values)

    print(Data)
    Result = list(filter(Ret,Data))

    print(Result)
    

if __name__ =="__main__":
    main()