Weight= int(input("Plz enter your weight kg:"))
Height= float(input("Plz enter your height cm:"))

BMI = Weight/ Height**2*10000

if BMI>35 :
    print("Extremely obese")
if BMI<= 35 and BMI>30:
    print("Obese")
if BMI<= 30 and BMI>25:
    print("overweight")
if BMI<= 25 and  BMI >18.5:
    print("Normal")
if BMI<= 18.5:
    print("underweight")


