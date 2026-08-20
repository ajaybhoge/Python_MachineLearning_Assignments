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

##################################################
#
#  Step 4 : Euclidean Distance Before And After Scaling
#
##################################################

print(Border)
print("Step 4 : Euclidean Distance Before And After Scaling")
print(Border)

Point1 = np.array([25,20000])
Point2 = np.array([35,80000])

Distance_Before = np.sqrt(np.sum((Point1 - Point2) ** 2))

Points = np.array([Point1,Point2])

ScaledPoints = scaler.transform(Points)

Distance_After = np.sqrt(
    np.sum((ScaledPoints[0] - ScaledPoints[1]) ** 2)
)

print("Point 1 :",Point1)
print("Point 2 :",Point2)

print("Euclidean Distance Before Scaling :",Distance_Before)
print("Euclidean Distance After Scaling :",Distance_After)

print("Before scaling, the larger numerical feature")
print("has a much larger effect on the distance.")
print("After scaling, the features are brought to a")
print("similar scale, so their contribution is more balanced.")

##################################################
#
#  Step 5 : Classification Report
#
##################################################

print(Border)
print("Step 5 : Classification Report")
print(Border)

print("A classification report gives important metrics")
print("for evaluating a classification model.")
print("It commonly contains precision, recall, F1-score")
print("and support for each class.")
print("It is used with classification models whose output")
print("contains classes or labels.")

##################################################
#
#  Step 6 : Classification Report Metrics
#
##################################################

print(Border)
print("Step 6 : Classification Report Metrics")
print(Border)

print("Precision : Out of the observations predicted as")
print("positive, it tells how many were actually positive.")

print("Recall : Out of the actual positive observations,")
print("it tells how many were correctly identified.")

print("F1 Score : It is the harmonic mean of precision and recall.")

print("Support : It is the number of actual observations")
print("belonging to each class.")

print("Accuracy : It is the proportion of correct predictions")
print("among all predictions.")
