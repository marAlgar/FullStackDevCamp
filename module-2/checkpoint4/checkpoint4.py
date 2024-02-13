import math

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)
float = 1.5
integer = 1
decimal = 1.7
dictionary = {'name': 'John', 'age': 25}

# Exercise 2: Round your float up.

print(math.ceil(float))

# Exercise 3: Get the square root of your float.

print(math.sqrt(float))

# Exercise 4: Select the first element from your dictionary.

print(dictionary['name'])

# Exercise 5: Select the second element from your tuple.

print(tuple[1])

# Exercise 6: Add an element to the end of your list.

list.append(6)
print(list)

# Exercise 7: Replace the first element in your list.

list[0] = 0
print(list)

# Exercise 8: Sort your list alphabetically.

list.sort()
print(list)

# Exercise 9: Use reassignment to add an element to your tuple.

tuple = tuple + (6,)
print(tuple)