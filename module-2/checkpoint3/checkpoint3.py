# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

string = "Hello World!"
number = 10
list = [1, 2, 3, 4, 5]
boolean = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

print(string[:3])

# Exercise 3: Use an index to grab the first element from your list.

print(list[0])

# Exercise 4: Create a new number variable that adds 10 to your original number.

new_number = number + 10
print(new_number)

# Exercise 5: Use an index to get the last element in your list.

print(list[-1])

# Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
print(names.split(','))

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

first_word = string[:5]
first_word = first_word.upper()
new_string = first_word + string[5:]
print(new_string)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

print(f"My number is {number}")

# Exercise 9: Print “hello world”.

print("hello world")



name = ‘Marcela’ 
string = f‘My name is {name}.’

print(string)