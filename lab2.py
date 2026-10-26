print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calc_bmi(ht, wt):
    print("value of height is: ", ht)
    print("value of weight is: ", wt)
    bmi = wt / (ht*ht)
    print("value of bmi is: ", bmi)
    return bmi

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

def display_main_menu():
    print("display_main_menu")

def calc_average():
    print("calc_average")

def get_user_input():
    print("User input")

if __name__ == "__main__":
    main()


bmi_ot = calc_bmi(2.06, 113)

if bmi_ot < 18.5:
    print("BMI is underweight")
elif bmi_ot >= 18.5 and bmi_ot <= 25:
    print("BMI is normal weight")
else:
    print("BMI is over weight")


print("BMI output is: ", bmi_ot)
