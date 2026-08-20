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
