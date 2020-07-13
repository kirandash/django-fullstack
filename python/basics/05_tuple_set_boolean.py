# Booleans
# True False 1 0

# Tuples
print('--- Tuples ---')
# Tuples are same as Lists - but are immutable
t = (1, 2, 3)
print(t[0])

t = ('a', True, 8789)
print(t)
# t[0] = 'New Item'  # Tuples are immutable like string
# Slicing, indexing and other methods for Tuples are same as List

# Sets
print('--- Sets ---')
x = set()

x.add(1)
x.add(2.3)
x.add(45.33)
x.add(0.009)
x.add(99.34)
print(x)  # similar to dictionary in {} but without key value pairs
# sets are unordered like a dictionary. So order may change every time

# sets are unique
x.add(2.3)  # can not be added since 2.3 is already present
print(x)  # contains only one 2.3

# Application - getting unique items from List
print('--- Getting unique items from List ---')
converted = set([2, 2, 2, 4, 5, 5, 5, 6, 6])
print(converted)
