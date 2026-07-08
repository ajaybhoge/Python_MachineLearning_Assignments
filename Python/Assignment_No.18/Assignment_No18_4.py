
def main():
    Value = int(input("Enter the Number :"))
    Data = []

    for i in range(1,Value+1):
        Values = int(input("Enter iput :"))
        Data.append(Values)

    
    print(Data)

    # Result = Data.count(5)
    # print(Result)

    Value2 = int(input("Enter iput to search:"))
    cnt = 0
    for i in Data:
        if i == Value2:
            cnt = cnt +1

    print(cnt)
    


if __name__ == "__main__":
    main()