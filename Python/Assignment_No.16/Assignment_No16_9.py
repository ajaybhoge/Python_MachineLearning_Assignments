
def main():
    Value =  int(input("Enter the Number :"))
    cnt =0
    for i in range(2,Value+1,2):
        print(i)
        cnt  = cnt +1
        if cnt == 10:
            break

if __name__ == "__main__":
    main()