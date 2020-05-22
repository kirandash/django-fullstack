# 10 to the power 5
print('--- 10 to the power 5 ---')
print(10**5)

# square root of 16
print('--- square root of 16 ---')
print(16**0.5)

# order of execution
print('--- order of execution ---')
print(4+8 * 10+2)

# paranthesis to control order of execution
print('--- paranthesis to control order of execution ---')
print((4+8) * (10+2))

# variable assignment with python
print('--- variable assignment with python ---')
# Python is a dynamic programming language and therefore we do not need to set variable types beforehand. variable types are auto declared when we assign a value
b = 10 # assigning values
print(b)
print(b*b)

# reassigning values
print('--- reassigning values ---')
b = b*9
print(b)

# Typecasting
print('--- Typecasting ---')
first_number = 50
second_number = 0.5
print(first_number * second_number) # integer * floating point = floating point - Python automatically converts data type for first_number to floating point as 50.0 and then multiply with second_number i.e. 0.5 So, we don't have to worry about mismatch in data types

# variable naming rules
print('--- variable naming rules ---')
# Rule 1: variable name can not start with numbers or special characters - will return invalid syntax
# 3name = 'kiran'
# Rule 2: variable names with multiple words should be named width snake casing unlike camelcasing in JavaScript. Not mandatory
my_first_name = 'Kiran' # best practice
myLastName = 'Dash' # not invalid but best practice to use snake casing
print(my_first_name + ' ' + myLastName)
