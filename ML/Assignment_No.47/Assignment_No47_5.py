Border = "-"*30

##################################################
#
#  Step 1 : Explain Coefficient
#
##################################################

print(Border)
print("Step 1 : Explain Coefficient")
print(Border)

print("A coefficient tells us how much the dependent variable changes")
print("when the input variable changes by one unit.")

print("Real Life Example :")
print("If a salary model has Experience coefficient 5000,")
print("then salary increases by about 5000 for one extra year")
print("of experience, when other variables remain constant.")

##################################################
#
#  Step 2 : Coefficient And Intercept
#
##################################################

print(Border)
print("Step 2 : Coefficient And Intercept")
print(Border)

print("Regression Model : Y = 8X + 15")
print("Coefficient = 8")
print("Intercept = 15")
print("The coefficient 8 means that Y increases by 8")
print("when X increases by 1.")

##################################################
#
#  Step 3 : Study Hours And Marks
#
##################################################

print(Border)
print("Step 3 : Study Hours And Marks")
print(Border)

print("Regression Model : Marks = 6 * StudyHours + 40")
print("Coefficient 6 means marks increase by 6")
print("for one additional study hour.")
print("Intercept 40 means predicted marks are 40")
print("when StudyHours is zero.")

OldHours = 1
NewHours = OldHours + 2

OldMarks = 6 * OldHours + 40
NewMarks = 6 * NewHours + 40

print("Marks at 1 Study Hour :",OldMarks)
print("Marks after increasing study by 2 hours :",NewMarks)
print("Increase in Marks :",NewMarks - OldMarks)

##################################################
#
#  Step 4 : Predicted Salary
#
##################################################

print(Border)
print("Step 4 : Predicted Salary")
print(Border)

Experience = [2,5,7]

for Year in Experience:
    Salary = 12 * Year + 25
    print("Experience :",Year)
    print("Predicted Salary :",Salary)
    print()

##################################################
#
#  Step 5 : Negative Coefficient
#
##################################################

print(Border)
print("Step 5 : Negative Coefficient")
print(Border)

print("Regression Equation : Y = -3X + 20")
print("The negative coefficient means Y decreases")
print("when X increases.")

print("When X increases by 1, Y decreases by 3.")

X_Value = 4
Y_Value = -3 * X_Value + 20

print("Value of Y when X = 4 :",Y_Value)

print("Predicted Salary Table")

for Year in [2,5,7]:
    Salary = -3 * Year + 20
    print(Year,Salary)
