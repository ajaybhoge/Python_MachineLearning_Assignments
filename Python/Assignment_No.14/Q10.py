Ret = lambda x,y,z: max(x,y,z)
def main():
    Value1= int(input("Enter a Number :"))
    Value2= int(input("Enter a Number :"))
    Value3= int(input("Enter a Number :"))

    print(Ret(Value1,Value2,Value3))

if __name__ == "__main__":
    main()