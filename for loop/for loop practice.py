# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == "tails":
        count = count+1

print("1. Number of heads:", count)

# 2. Print square of all numbers between 1 to 10 except even numbers

print('2. ...................')
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
        print(i)

# 3. Write a program that asks you to enter an expense amount and program should tell you in which month
# that expense occurred. If expense is not found then it should print that as well.
print('3.  ....................')
import calendar
expense_list = [2340, 2500, 2100, 3100, 2980]
amount = int(input("Enter amount:"))

if amount in expense_list:
    month_index = expense_list.index(amount)
    month_name = calendar.month_name[month_index+1]
    print("Expense of the month: ", month_name, "is", amount)
else:
    print("Amount not found! ")

