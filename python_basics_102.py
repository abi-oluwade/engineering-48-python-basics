# Strings!

## Define strings - using '' and ""
my_string = "This is a string"
my_string2 = 'So am I'
my_animal = "Mouse"

print(my_string)
print(type(my_string2))

## Concatenation - joining of two strings
print("Wow so " + my_string + "This is an example of concatenation")
print("These are examples of strings", my_string2, my_string)

concatenate = my_string + " " + my_string2 + " " + my_animal
print(concatenate)

## Interpolation (getting a variable or piece of code into a string)
age = 23
name = "Abi"

### This is where we need to interpolate
print("Welcome <person>, you are <age_years> old")
print("Welcome <person>, you were born on the year <date_birth>")

### This is us actually interpolating values ( we put the f in the statement to format it and add the variables)
print(f"Welcome {name}, you are {age} old")
print(f"Welcome {name}, you were born on the year {2019 - age}")

print("Welcome name {}, you were born on the year {}".format(name,age))

## Useful methods for strings (a method is dependant on a single datatype)
example_string = " HELLoo "
print(example_string)

print(example_string.strip()) # removes trailing white spaces (strip)
print(example_string.count('L')) # count number of chracters in string
print(example_string.lower()) # prints the string in lower case( and use .upper for upper case)
print(example_string.strip().capitalize()) # chaining methods

## standard builtin function len() (example of function that is not dependant on the object that is the string)

## the 'delimter' is where it seperates in a string, learning and using .split(), 'self' means the function is waiting for the object of a certain datatype
text_to_split = ("This is some example text in our file")
result_split = text_to_split.split(" ")
print(result_split)
result_split2 = text_to_split.split("I")
print(result_split2)

## Casting and int
str_string = "1995"
print(type(str_string))

### str --> int
int_number = int(str_string)
print(type(int_number))

### int --> str
new_str = str(int_number)
print(new_str)