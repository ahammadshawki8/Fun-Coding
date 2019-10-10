# making a BMR calculater

name=input("what is your name? -->")
sex=input("are you a male or female? -->")
age=int(input("how old are you? -->"))
height=float(input("what is your height? -->"))
weight=int(input("what is your weight? -->"))

def ft2cm(height):
    import math
    a=(math.floor(height)*12)
    b=(height-(a/12))*12
    c=a+b
    height_cm=c*2.54
    return height_cm
def bmr_calculater(name,weight,height_cm,sex,age):
    if sex=="girl":
        bmr=655+(9.6*weight)+(1.8*height_cm)-(4.7*age)
    else:
        bmr=66+(13.7*weight)+(5*height_cm)-(6.8*age)
    messege= name.capitalize()+"\'s bmr is "+str(bmr)
    return messege
    
height_cm=ft2cm(height)
print("\n")
print(bmr_calculater(name,weight,height_cm,sex,age))
