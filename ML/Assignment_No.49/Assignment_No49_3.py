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

##################################################
#
#  Step 2 : Calculate Variance And Standard Deviation
#
##################################################

print(Border)
print("Step 2 : Calculate Variance And Standard Deviation")
print(Border)

Variance = np.var(Data)
StandardDeviation = np.std(Data)

print("Variance :",Variance)
print("Standard Deviation :",StandardDeviation)

##################################################
#
#  Step 3 : Feature Scaling Using StandardScaler
#
##################################################

from sklearn.preprocessing import StandardScaler

print(Border)
print("Step 3 : Feature Scaling Using StandardScaler")
print(Border)

Data2 = np.array([
    [25,20000],
    [30,40000],
    [35,80000]
])

scaler = StandardScaler()

ScaledData = scaler.fit_transform(Data2)

print("Original Dataset :")
print(Data2)

print("Scaled Dataset :")
print(ScaledData)
