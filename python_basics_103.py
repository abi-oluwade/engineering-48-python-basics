# Numerical types
## Numerical types are : integers, floats, composite
    ## big ints and complex numbers

## declaring an int

num1 = 20
print(type(num1))

num2 = 20.0
print(type(num2))

##  Operators,  +,  -,  *,  /,  %, in (these take priority over logical operators)

result1 = 10 + 15
result2 = 10 - 2
result3 = 10 * 30
result4 = 20 % 3
result5 = 20 / 2

print(result1,result2,result3,result4,result5)

## Logical Operators, <,> (less than and more than) and >= and <= (represents more than or equal two and vice versa)
## (= is assignment == is equals)

num_a = 10
num_b = 10
num_c = 13

## logical operators here return Booleans expressions (expressions which can only be represented as true or false)

print(num_b > num_c)
print(num_a == num_b)
print (num_a >= num_b)
print ((num_a + num_b) > num_c)  ### This example here uses brackets to presever the mathmatical priority

## Check if the same
### data type matters ( 10 the int is not the same as "10" the string)

print ("10" == 10)
print(num_a == num_c)
print(num_a == num_c)

## Booleans are expressions which are either true or false.
print(type(True))
print(type(False))

bool_true = True
bool_false = False

print(bool_true != bool_true)
print(bool_true == bool_true)

## Logical AND & logical OR
## AND syntax takes the (<condition>) AND (<condition>) ---> outputs a bool
    ## requires the two sides to be true in order for it to return true.
print(True and True) ### the two sides are true
print(True and False) ### only one side is true ---> becomes false

## OR  syntax takes the (<condition>) OR (<condition>) ---> outputs a bool
    ## requires only side to be true to result in true

print(True or False)
print(False or True)
print(False or False)


