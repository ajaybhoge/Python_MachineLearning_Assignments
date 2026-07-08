Ret = lambda x,y: x if x>y else y
def main():
    Value1= int(input("Enter a Number :"))
    Value2= int(input("Enter a Number :"))

    print(Ret(Value1,Value2))
if __name__ == "__main__":
    main()