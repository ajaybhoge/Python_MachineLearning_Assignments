import Arithemetic

def FactorAdd(No):
    Ans =  0
    for i in range(1,No):
        if No % i == 0:
            Ans = Ans + i
    print(Ans)


def main():
    Value1= int(input("Enter Number to get Factors Addition :"))

    FactorAdd(Value1)

if __name__ =="__main__":
    main()
