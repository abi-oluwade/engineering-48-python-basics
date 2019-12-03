# While loops and if statements

## syntax example (need a condtion in the loop that at some point will be met so the loops breaks and stops repeating.
## while <condition>:
    ## block of code
    ## block of code
    ## break when condition is fulfilled
##:

## note length is not the same as the index and heres a basic example

num = 0
while num < 10:
    print("still less than 10")
    num += 1

## you can iterate with the += which you can use to add 1 for example or whatever value tou put into it.

## using to substitute the for loop
wish_list = ["rc car","cheese","cheerleaders","white shirts", "sugar laces","reeses pieces"]
index_length = len(wish_list)-1
print(len(wish_list))
counter = 0

while counter <= index_length:
    print(wish_list[counter])
    counter += 1

while True:
