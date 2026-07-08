def CheckNumber(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    Value = int(input("Enter the Number to Check Number is :"))

    Ret =CheckNumber(Value)

    print(Ret)

if __name__ == "__main__":
    main()