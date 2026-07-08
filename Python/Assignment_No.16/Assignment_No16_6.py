def CheckNumber(No):
    if No > 0:
        print(f"{No} is Positive Number")
    elif(No<0):
        print(f"{No} is Negative Number")
    else:
        print("Number is Zero")

def main():
    Value = int(input("Enter the Number to Check Number is :"))

    CheckNumber(Value)

if __name__ == "__main__":
    main()