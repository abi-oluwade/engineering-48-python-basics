# Functions

# a function is like a machine, needs to be turned on (called)
# and it does things (block of code)
# NEVER print inside a function., call the function inside a print(function_name)

# Good practises
# They should be:
    #readable
    #maintainable
    #testable
    #avoid string code
# Dont repeat yourself
# Seperation of concerns
    # Define functions in one file
    # call them in another

# functions work this way
    # 1) define a function
    # 2) call the function

# syntax
# def <name>(arg, arg2,aeg3):
    # block of code
    # return something

def say_hello():
    return 'Hello'

say_hello()

def say_hello_user(fname,lname):
    return 'hello' + " " + fname + " " + lname

print(say_hello_user("Abi", "Oluwade"))