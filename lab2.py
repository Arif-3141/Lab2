print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calc_bmi(ht, wt):
    print("value of height is: ", ht)
    print("value of weight is: ", wt)
    bmi = round(wt / (ht*ht), 2)
    print("value of bmi is: ", bmi)
    if bmi < 18.5:
        value = -1
    elif bmi >= 18.5 and bmi <= 25:
        value = 0
    else:
        value = 1
    return bmi, value


bmi, weightClass = calc_bmi(2.06, 83)

if weightClass == -1:
    print("BMI is underweight")
elif weightClass == 0:
    print("BMI is normal weight")
else:
    print("BMI is over weight")

print("BMI output is: ", bmi, weightClass)