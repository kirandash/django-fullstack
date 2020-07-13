# Creating a Dictionary
print('--- Creating a Dictionary ---')
my_dict = {"key1": "value1", "key2": "value2",
           "key3": {'123': [1, 2, 'select me']}}
print(my_dict)
print(my_dict['key2'])
print(my_dict['key3']['123'][2])  # in dictionary, values are retrieved using
# the key, In List, values are retrieved using index

# can call methods after retrieving data
print(my_dict['key3']['123'][2].upper())

print('--- Mutating Dictionary ---')
my_dict2 = {'lunch': 'chicken', 'dinner': 'prawn'}
print(my_dict2)
my_dict2['lunch'] = 'pork'
print(my_dict2)
