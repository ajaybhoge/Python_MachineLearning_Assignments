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

##################################################
#
#  Step 2 : Calculate Model Performance
#
##################################################

print(Border)
print("Step 2 : Calculate Model Performance")
print(Border)

Y_Pred = m * X + c

print("Predicted Y Values :")
print(Y_Pred)

Error = Y - Y_Pred
SquaredError = Error ** 2

print("Errors :")
print(Error)

print("Squared Errors :")
print(SquaredError)

MSE = np.mean(SquaredError)

SS_Total = np.sum((Y - Y_mean) ** 2)
SS_Residual = np.sum((Y - Y_Pred) ** 2)

R2 = 1 - (SS_Residual / SS_Total)

print("Mean Squared Error :",MSE)
print("R2 Score :",R2)

##################################################
#
#  Step 3 : Salary Prediction And Regression Line
#
##################################################

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print(Border)
print("Step 3 : Salary Prediction And Regression Line")
print(Border)

Experience = np.array([1,2,3,4,5]).reshape(-1,1)
Salary = np.array([20000,25000,30000,35000,40000])

model = LinearRegression()

model.fit(Experience,Salary)

NewExperience = np.array([[6]])

Prediction = model.predict(NewExperience)

print("Predicted Salary for 6 Years Experience :",Prediction[0])

Salary_Prediction = model.predict(Experience)

plt.scatter(Experience,Salary)

plt.plot(Experience,Salary_Prediction)

plt.title("Experience Vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()

##################################################
#
#  Step 4 : Why KNN Is Called A Lazy Learner
#
##################################################

print(Border)
print("Step 4 : Why KNN Is Called A Lazy Learner")
print(Border)

print("KNN is called a lazy learner because it does not")
print("build a model during the training phase.")
print("It stores the training data and performs calculation")
print("when a new data point is given.")

##################################################
#
#  Step 5 : If K Is Too Small
#
##################################################

print(Border)
print("Step 5 : If K Is Too Small")
print(Border)

print("If K is too small, the model becomes sensitive")
print("to noise and individual data points.")
print("It may overfit the training data.")

##################################################
#
#  Step 6 : If K Is Too Large
#
##################################################

print(Border)
print("Step 6 : If K Is Too Large")
print(Border)

print("If K is too large, the model considers many")
print("data points and may ignore local patterns.")
print("It may underfit the data.")

##################################################
#
#  Step 7 : Why Linear Regression Minimizes Squared Error
#
##################################################

print(Border)
print("Step 7 : Why Linear Regression Minimizes Squared Error")
print(Border)

print("Linear Regression uses squared error so that")
print("positive and negative errors do not cancel each other.")
print("Squaring also gives more importance to larger errors.")

##################################################
#
#  Step 8 : MSE And R2 Difference
#
##################################################

print(Border)
print("Step 8 : MSE And R2 Difference")
print(Border)

print("MSE measures the average squared difference")
print("between actual and predicted values.")
print("Lower MSE generally means smaller prediction errors.")

print("R2 measures how much of the variation in the")
print("dependent variable is explained by the model.")
print("A value closer to 1 generally indicates better fit.")
