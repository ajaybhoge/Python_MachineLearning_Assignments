def ChkPrime(No1):
    Data  =[]
    for i in No1:
        Cnt = False
        for j in range(2,int(i/2)+1):
            if i % j == 0:
                Cnt = True
        if Cnt == False:
            Data.append(i)
    return Data