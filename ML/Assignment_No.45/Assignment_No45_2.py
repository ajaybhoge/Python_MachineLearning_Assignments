import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*30

##################################################
#
#  Step 1 : Normalize Math Scores Using Min-Max Scaling
#
##################################################

print(Border)
print("Step 1 : Normalize Math Scores Using Min-Max Scaling")
print(Border)

data = {
    "Name" : ["Amit","Sagar","Pooja"],
    "Math" : [85,90,78],
    "Science" : [92,88,80],
    "English" : [75,85,82]
}

df = pd.DataFrame(data)

df["Math_Normalized"] = (
    (df["Math"] - df["Math"].min()) /
    (df["Math"].max() - df["Math"].min())
)

print(df)

##################################################
#
#  Step 2 : Create Gender Column And One Hot Encoding
#
##################################################

print(Border)
print("Step 2 : Create Gender Column And One Hot Encoding")
print(Border)

df["Gender"] = ["Male","Male","Female"]

print("DataFrame With Gender")
print(df)

df = pd.get_dummies(df,columns = ["Gender"])

print("DataFrame After One Hot Encoding")
print(df)
