import statistics as stat

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_lst = get_user_input()
    avg = calc_average_temperature(num_lst)
    min_max = find_min_max_temperature(num_lst)
    median = calc_median_temperature(num_lst)
    print("\nNumber list: ", num_lst)
    print("Average: ", avg)
    print("Minimum and Maximum: ", min_max)
    print("Median: ", median)



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
    avg = round(sum/len(lst),2)
    return avg

def calc_median_temperature(lst):
    sorted_lst = sort_temperature(lst)
    return stat.median(sorted_lst)

def find_min_max_temperature(lst):
    max, min = 0, 99999
    for i in lst:
        if max < i:
            max = i
        if min > i:
            min = i
    min_max = [min, max]
    return min_max
    

def sort_temperature(lst):
    return sorted(lst)


if __name__ == "__main__":
    main()
