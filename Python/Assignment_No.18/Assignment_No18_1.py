from functools import reduce
def Add(x,y):
    Ans = x+y
    return Ans


def main():
    Value = int(input("Enter the Number :"))
    Data = []

    for i in range(1,Value+1):
        Values = int(input("Enter iput :"))
        Data.append(Values)

    print(Data)

    Result = reduce(Add,Data)

    print(Result)
    


if __name__ == "__main__":
    main()