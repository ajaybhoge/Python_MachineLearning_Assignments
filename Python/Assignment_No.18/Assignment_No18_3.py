from functools import reduce

# Max = lambda x , y: x if x>y else y
def Max(x,y):
    if x<y:
        return x
    else:
        return y

def main():
    Value = int(input("Enter the Number :"))
    Data = []

    for i in range(1,Value+1):
        Values = int(input("Enter iput :"))
        Data.append(Values)

    print(Data)

    Result = reduce(Max,Data)

    print(Result)
    


if __name__ == "__main__":
    main()