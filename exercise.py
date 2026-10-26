def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_lst = get_user_input()
    avg = calc_average_temperature(num_lst)
    min_max = find_min_max_temperature(num_lst)
    print(num_lst)
    print(avg)
    print(min_max)



def display_main_menu():
    print("\nArif's code\n\nEnter a sequence of floats")

def get_user_input():
    user_lst = input("User input: ").split(",")
    final_lst = []
    for i in user_lst:
        final_lst.append(float(i))
    return final_lst

def calc_average_temperature(lst):
    sum = 0.0
    for i in lst:
        sum += i
    avg = sum/len(lst)
    return avg

def calc_median_temperature(lst):
    median = int(len(lst)/2)
    value = lst[median]
    return value

def find_min_max_temperature(lst):
    max, min = 0, 99999
    for i in lst:
        if max < i:
            max = i
        if min > i:
            min = i
    min_max = [min, max]
    return min_max
    

def sort_temperature():
    print("")


if __name__ == "__main__":
    main()
