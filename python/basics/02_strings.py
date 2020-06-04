# String syntax
print('--- String Syntax ---')
print('Hello World!')
print("Hello World!")

# Escaping single/double quotes
print('--- Escaping single/double quotes ---')
print("I'm Kiran")
print('Hello "Kiran"')

# Indexing
print('--- Indexing ---')
myName = 'Kiran Kumar Dash'
print(myName)
print(myName[0])  # k
print(myName[-1])  # h (python supports negative indexing, goes back in loop)
print(myName[5])  # empty space is also a character

# Slicing
print('--- Slicing ---')
print(myName[2:])  # slice everything starting from 2 till end, 2 included
print(myName[:3])  # slice everything from start up to 3, 3rd not included
print(myName[2:5])  # slice starting from 2 up to 5, 5th not include
print(myName[:])  # will return everything starting from start to end
print(myName[::1])  # step size of 1 returns everything, jumps 1 step at a time
print(myName[::2])  # step size of 2, jumps 2 steps at a time
print(myName[::5])  # step size of 2, jumps 5 steps at a time

# Stings are immutable
print('--- Stings are immutable ---')
# myName[0] = 'i'  # 'str' object does not support item assignment
myName = 'Kiran Dash'
print(myName)  # can re-assign entire variable but can't mutate items

# Useful Methods
print('--- Useful Methods ---')
upName = myName.upper()  # returns a copy of string, converted to uppercase
print(upName)

lowName = myName.lower()  # Note: returns a copy, original is not affected
print(lowName)

capName = myName.capitalize()  # capitalizes first letter and rest small
print(capName)

# Split
print('--- Split ---')
s = myName.split()  # by default split will split data based on empty string &
# return a list
print(s)  # will return kiran and dash
print("kirandash".split())  # will return kirandash as single string

commaString = 'tea,coffee'
commaList = commaString.split(',')
print(commaList)  # return a list after splitting based on comma

# Print Formatting
print('--- Print Formatting ---')
# Insert One string
someText = "Insert my full name at the " \
           "end of this string: {}".format("Kiran Kumar Dash")
print(someText)

# Insert Two Strings
someText2 = "Insert First Name: {}. " \
            "Insert Last Name: {}".format("Kiran", "Dash")
print(someText2)  # strings are inserted based on order


# Insert multiple strings with mapped variable names
someText3 = "Insert here: {b}. Insert here: {a}. Insert here: {c}"\
    .format(a="Kumar", b="Kiran", c="Dash")  # No need to follow order. Best
print(someText3)

# Insert repeatedly with mapped variable names
someText4 = "Insert here: {x}. Insert here: {x}. Insert here: {y}"\
    .format(x="Dash", y="Python")  # No need to follow order.
print(someText4)
