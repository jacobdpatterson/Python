# - Can take a list and run each item through a function

income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

map(double_money, income) #What function will you run your items through, what is the list. Doubles money no output.

new_income = list(map(double_money, income)) #What function will you run your items through, what is the list
print(new_income)