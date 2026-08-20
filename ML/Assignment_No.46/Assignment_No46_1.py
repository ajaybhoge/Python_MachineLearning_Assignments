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
