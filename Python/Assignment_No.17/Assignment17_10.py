def Pattern(No):
    cnt = 0
    while(No != 0):
        NO1 = No % 10
        cnt = cnt + NO1
        No = No // 10

    return cnt       
def main():
    Value1= int(input("Enter First Number :"))
    Ret = Pattern(Value1)
    print(Ret)


if __name__ == "__main__":
    main()