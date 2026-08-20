import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Border = "-"*30

##################################################
#
#  Step 1 : Create DataFrame
#
##################################################

print(Border)
print("Step 1 : Create DataFrame")
print(Border)

data = {
    "Name" : ["Amit","Sagar","Pooja"],
    "Math" : [85,90,78],
    "Science" : [92,88,80],
    "English" : [75,85,82]
}

df = pd.DataFrame(data)

print("DataFrame Created Successfully")
print(df)

##################################################
#
#  Step 2 : Display Descriptive Statistics
#
##################################################

print(Border)
print("Step 2 : Display Descriptive Statistics")
print(Border)

print(df.describe())

##################################################
#
#  Step 3 : Add Total Column
#
##################################################

print(Border)
print("Step 3 : Add Total Column")
print(Border)

df["Total"] = df["Math"] + df["Science"] + df["English"]

print("DataFrame After Adding Total")
print(df)
