# local variables are in small case and only "_" is allowed and no special characters even space is not allowed.
# global variables are in capital letters.
# Python uses Dynamic typing = reassign variables to different data types.

a = 5
print(a)
print(type(a))

a = 10.5
print(a)
print(type(a))

a = 'today is wednesday'
print(a)
print(type(a))

print(a +" " + a)

a = 10.5
a = a + a
print(a)
print(type(a))

my_income = 100
my_tax_rate = 0.1
my_tax = my_income * my_tax_rate
my_take_home = my_income - my_tax
print("my tax for the current FY is ",my_tax)
print("my my_take_home salary for the current FY is ",my_take_home)


