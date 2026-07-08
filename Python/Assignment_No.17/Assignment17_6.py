def Pattern(No):
    Ans = 0
    for i in range(No,0,-1):
        for j in range(1,i+1):
            print(" * ", end = "   ")
        print("")

def main():
    Value1= int(input("Enter First Number :"))
    Pattern(Value1)

if __name__ == "__main__":
    main()