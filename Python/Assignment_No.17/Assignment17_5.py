def PrimeNumbCheck(No):
    Ans = False
    for i in range(2,int(No/2)):
        if No % i == 0:
            Ans = True
    if Ans == True:
        print("It is prime Number")
    else:
        print("It is not prime Number")


def main():
    Value1= int(input("Enter Number  :"))

    PrimeNumbCheck(Value1)

if __name__ =="__main__":
    main()
