import numpy as np

Border = "-"*30

##################################################
#
#  Step 1 : Calculate Mean
#
##################################################

print(Border)
print("Step 1 : Calculate Mean")
print(Border)

Data = np.array([6,7,8,9,10,11,12])

Mean = np.mean(Data)

print("Dataset :",Data)
print("Mean :",Mean)
