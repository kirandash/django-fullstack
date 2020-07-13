# Creating a List
print('--- Creating a List ---')
myList = [1, 2, 3]
print(myList)

myList2 = ['somestring', 1, 2, 23.456, True, 'asdf', [1, 2, 3]]
print(myList2)

# Length of a List
print('--- Length of a List ---')
print(len(myList2))  # 7

# Indexing in a List - same as string
print('--- Indexing in a List ---')
print(myList2[0])  # first item in List
print(myList2[-1])  # last item in List

# Slicing a List - same as string
print('--- Slicing a List ---')
print(myList2[2:])  # slice everything starting from 2 till end, 2 included
print(myList2[:3])  # slice everything from start up to 3, 3rd not included
print(myList2[2:5])  # slice starting from 2 up to 5, 5th not include

# Adding Items to List - Unlike strings, Lists are mutable
print('--- Adding Items to List ---')
myList2[0] = 'NEW ITEM'
print(myList2)

# Basic List methods
print('--- adding items to List with append and extend methods ---')
myList2.append("NEW END ITEM")
print(myList2)

myList2.append(["x", "y", "z"])
print(myList2)  # will append the new item as a List

myList2.extend(["x", "y", "z"])  # will extend the List to add new items
print(myList2)

print('--- remove items from List with pop method ---')
# Note: pop method returns an item
removedItem = myList2.pop()  # by default removes the last item
print(removedItem)
print(myList2)

remItem = myList2.pop(0)  # index of item to pop
print(remItem)
print(myList2)

print('--- reverse method ---')
myList2.reverse()
print(myList2)

print('--- sort method ---')
listWithNumbers = [4, 89, 3, 1, 888]
listWithNumbers.sort()
print(listWithNumbers)

print('--- Nested List ---')
nestedList = [1, 2, ['x', 'y', 'z']]
print(nestedList[2][1])

print('--- List comprehension ---')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in matrix]
print(first_col)
