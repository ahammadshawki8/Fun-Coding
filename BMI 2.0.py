# BMI without function

name =input("enter your name: ").capitalize()
height_m =float(input("enter your height in metre: "))
weight_kg =float(input("enter your weight in kilogram: "))

bmi=weight_kg/(height_m**2)
print("bmi: ")
print(bmi)

if bmi < 25:
    print(name+" is not overweight.")
else:
    print(name+" is overweight.")