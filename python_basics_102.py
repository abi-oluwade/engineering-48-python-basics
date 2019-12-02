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
print(f"Welcome {name}, you are <{age} old")
print(f"Welcome {name}, you were born on the year {2019 - age}")

## Useful methods for strings (a method is dependant on a single datatype)