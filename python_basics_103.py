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