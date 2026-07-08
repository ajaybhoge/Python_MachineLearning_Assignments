Ret = lambda x: x*x
def main():
    Value= int(input("Enter the Number : "))
    Data = []

    for i in range(1, Value+1):
        Values = int(input("Enter the Numbers : "))
        Data.append(Values)

    print(Data)
    Result = list(map(Ret,Data))

    print(Result)
    

if __name__ =="__main__":
    main()