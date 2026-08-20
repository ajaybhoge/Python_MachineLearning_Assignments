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

##################################################
#
#  Step 3 : Group Students By Gender
#
##################################################

print(Border)
print("Step 3 : Group Students By Gender")
print(Border)

data_gender = {
    "Name" : ["Amit","Sagar","Pooja"],
    "Math" : [85,90,78],
    "Science" : [92,88,80],
    "English" : [75,85,82],
    "Gender" : ["Male","Male","Female"]
}

GenderData = pd.DataFrame(data_gender)

GenderData["Total"] = (
    GenderData["Math"] +
    GenderData["Science"] +
    GenderData["English"]
)

print(GenderData.groupby("Gender")[["Math","Science","English","Total"]].mean())

##################################################
#
#  Step 4 : Pie Chart Of Subject Marks For Sagar
#
##################################################

print(Border)
print("Step 4 : Pie Chart Of Subject Marks For Sagar")
print(Border)

Sagar = [90,88,85]
Subjects = ["Math","Science","English"]

plt.pie(Sagar,labels = Subjects,autopct = "%1.1f%%")

plt.title("Subject Marks Of Sagar")

plt.show()

##################################################
#
#  Step 5 : Add Status Column
#
##################################################

print(Border)
print("Step 5 : Add Status Column")
print(Border)

data_status = {
    "Name" : ["Amit","Sagar","Pooja"],
    "Math" : [85,90,78],
    "Science" : [92,88,80],
    "English" : [75,85,82]
}

StatusData = pd.DataFrame(data_status)

StatusData["Total"] = (
    StatusData["Math"] +
    StatusData["Science"] +
    StatusData["English"]
)

StatusData["Status"] = StatusData["Total"].apply(
    lambda x : "Pass" if x >= 250 else "Fail"
)

print(StatusData)

##################################################
#
#  Step 6 : Count Passed Students
#
##################################################

print(Border)
print("Step 6 : Count Passed Students")
print(Border)

Passed = (StatusData["Status"] == "Pass").sum()

print("Number of Passed Students :",Passed)

##################################################
#
#  Step 7 : Export Final DataFrame To CSV
#
##################################################

print(Border)
print("Step 7 : Export Final DataFrame To CSV")
print(Border)

StatusData.to_csv("student_marks_final.csv",index = False)

print("Final DataFrame Exported Successfully")
print("File Name : student_marks_final.csv")

##################################################
#
#  Step 8 : Histogram Of Math Marks
#
##################################################

print(Border)
print("Step 8 : Histogram Of Math Marks")
print(Border)

plt.hist(StatusData["Math"])

plt.title("Distribution Of Math Marks")
plt.xlabel("Math Marks")
plt.ylabel("Number Of Students")

plt.show()

##################################################
#
#  Step 9 : Rename Math Column
#
##################################################

print(Border)
print("Step 9 : Rename Math Column")
print(Border)

StatusData = StatusData.rename(columns = {"Math":"Mathematics"})

print(StatusData)
