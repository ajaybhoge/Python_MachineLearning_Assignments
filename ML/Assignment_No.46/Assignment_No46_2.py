import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

Border = "-"*30

##################################################
#
#  Step 1 : Get Data
#
##################################################

print(Border)
print("Step 1 : Get Data")
print(Border)

DataPath = "MarvellousAdvertising.csv"

df = pd.read_csv(DataPath)

print("Dataset Loaded Successfully")
print(df)

##################################################
#
#  Step 2 : Clean, Prepare And Manipulate Data
#
##################################################

print(Border)
print("Step 2 : Clean, Prepare And Manipulate Data")
print(Border)

df.dropna(inplace = True)

X = df.drop(columns = ["sales"])
Y = df["sales"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)

print("Input Columns :",X.columns.tolist())
print("Output Column : sales")
