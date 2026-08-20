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

##################################################
#
#  Step 3 : Train Data
#
##################################################

print(Border)
print("Step 3 : Train Data")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,test_size = 0.5,random_state = 42
)

print("Training Data Shape :",X_train.shape)
print("Testing Data Shape :",X_test.shape)

model = LinearRegression()

print("Model gets Created Successfully")

model.fit(X_train,Y_train)

print("Model Trained Successfully")

##################################################
#
#  Step 4 : Test The Data
#
##################################################

print(Border)
print("Step 4 : Test The Data")
print(Border)

Y_pred = model.predict(X_test)

print("Model Testing Done")
