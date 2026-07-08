Ret = lambda x:x if (len(x) >= 5) else False
def main():
    Value= int(input("Enter the String : "))
    Data = []

    for i in range(1, Value+1):
        Values =input("Enter the String : ")
        Data.append(Values)

    print(Data)
    Result = list(filter(Ret,Data))

    print(Result)
    

if __name__ =="__main__":
    main()