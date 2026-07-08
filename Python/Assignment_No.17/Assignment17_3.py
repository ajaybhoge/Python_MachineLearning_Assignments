import Arithemetic

def Fact(No):
    Ans =  1
    for i in range(1,No+1):
        Ans = Ans *i
    
    return Ans


def main():
    Value1= int(input("Enter First Number :"))

    Ret = Fact(Value1)

    print(Ret)

if __name__ =="__main__":
    main()
