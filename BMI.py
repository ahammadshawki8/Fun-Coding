# making bmi calculater
name1="Joe"
height_m1=1.75
weight_kg1=70

name2="Sarah"
height_m2=1.6
weight_kg2=75

name3="Frank"
height_m3=2
weight_kg3=165

def bmi_calculater(name,height_m,weight_kg):
        bmi=weight_kg/(height_m**2)
        print(bmi)
        if bmi<25:
                result=name+" is not overweight"
        else:
                result=name+" is overweight"
        return result
result1= bmi_calculater(name1,height_m1,weight_kg1)
print(result1)
result2= bmi_calculater(name2,height_m2,weight_kg2)
print(result2)
result3= bmi_calculater(name3,height_m3,weight_kg3)
print(result3)