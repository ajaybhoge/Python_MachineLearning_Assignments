from functools import reduce  

Ret = lambda x,y:x if x < y else y
def main():
    Value= int(input("Enter the Number : "))
    Data = []

    for i in range(1, Value+1):
        Values = int(input("Enter the Numbers : "))
        Data.append(Values)

    print(Data)
    Result = reduce(Ret,Data) #sum = sum + Data[i]
 
    print("The Minimum Number is",Result)
    

if __name__ =="__main__":
    main()