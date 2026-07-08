from functools import reduce
from MarvellousNum import ChkPrime

Ret = lambda x,y : x+y
def main():
    Value = int(input("Enter the Number :"))
    Data = []

    for i in range(1,Value+1):
        Values = int(input("Enter iput :"))
        Data.append(Values)

    Result = ChkPrime(Data)
    print(Result)

    Result2 = reduce(Ret,Result)

    print(f"Addition is :{Result2}")
    

if __name__ == "__main__":
    main()