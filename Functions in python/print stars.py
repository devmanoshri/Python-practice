# print * pattern from a function
def print_stars(line_no):
    s = ''
    for i in range(int(line_no)):
        for j in range(i):
            s = s + '*'
            print(s)

line_val = input("Enter how many line you want to print:")
print("Here we go.....")
print(print_stars(line_val))






