Ret = lambda x: True if x % 2 != 0 else False
def main():
    Value= int(input("Enter a Number :"))

    print(Ret(Value))

if __name__ == "__main__":
    main()