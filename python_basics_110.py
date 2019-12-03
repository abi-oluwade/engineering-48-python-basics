#Functions

## A function is a block of code which only runs when it is called, you can pass data, known as parameters into the
## function. A function can return data as a result

## Syntax
## if <condition>:
    ## block of code
## elif <condition>
    ## block of code
## else:
    ## block of code

## example 2
age = 18

if age >= 18 and age > 18:
    print ('you can vote and watch 18 rated movies')
elif age >= 16:
    print ('you can nearly vote!')
else:
    print("You cannot vote")

age = int(input("What is you age?"))

## example 2 of if,else and elif
if age < 21 and age > 18:
    print("you can vote but cannot drink")
elif age > 18:
    print("You can vote!")
elif age >= 16:
    print("you can drive in the US")
else:
    print("you are a child")

## the most specific conditions have to be at the top, and is built with logical operators and mathmatical operators
## once something is true the block runs and the program exits the function.