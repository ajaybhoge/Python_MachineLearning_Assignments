import numpy as np

Border = "-"*30

##################################################
#
#  Step 1 : Simple Linear Regression Manually
#
##################################################

print(Border)
print("Step 1 : Simple Linear Regression Manually")
print(Border)

X = np.array([1,2,3,4,5])
Y = np.array([3,4,2,4,5])

X_mean = np.mean(X)
Y_mean = np.mean(Y)

Numerator = np.sum((X - X_mean) * (Y - Y_mean))
Denominator = np.sum((X - X_mean) ** 2)

m = Numerator / Denominator
c = Y_mean - (m * X_mean)

print("Mean of X =",X_mean)
print("Mean of Y =",Y_mean)
print("Slope (m) =",m)
print("Intercept (c) =",c)

print("Regression Equation :")
print("Y =",m,"X +",c)

X_New = 6
Y_New = m * X_New + c

print("Predicted Y for X = 6 :",Y_New)
