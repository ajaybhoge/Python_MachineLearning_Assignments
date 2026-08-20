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

##################################################
#
#  Step 4 : Students With Science Marks More Than 85
#
##################################################

print(Border)
print("Step 4 : Students With Science Marks More Than 85")
print(Border)

Result = df[df["Science"] > 85]

print(Result)

##################################################
#
#  Step 5 : Replace Pooja With Puja
#
##################################################

print(Border)
print("Step 5 : Replace Pooja With Puja")
print(Border)

df["Name"] = df["Name"].replace("Pooja","Puja")

print(df)

##################################################
#
#  Step 6 : Sort DataFrame By Total Marks
#
##################################################

print(Border)
print("Step 6 : Sort DataFrame By Total Marks")
print(Border)

df = df.sort_values(by = "Total",ascending = False)

print(df)

##################################################
#
#  Step 7 : Bar Plot Of Student Names Vs Total Marks
#
##################################################

print(Border)
print("Step 7 : Bar Plot Of Student Names Vs Total Marks")
print(Border)

plt.bar(df["Name"],df["Total"])

plt.title("Student Names Vs Total Marks")
plt.xlabel("Student Names")
plt.ylabel("Total Marks")

plt.show()

##################################################
#
#  Step 8 : Line Chart For Amit
#
##################################################

print(Border)
print("Step 8 : Line Chart For Amit")
print(Border)

Amit = df[df["Name"] == "Amit"].iloc[0]

Subjects = ["Math","Science","English"]
Marks = [Amit["Math"],Amit["Science"],Amit["English"]]

plt.plot(Subjects,Marks,marker = "o")

plt.title("Marks of Amit")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
