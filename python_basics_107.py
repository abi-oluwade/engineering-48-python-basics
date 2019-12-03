#FOR LOOPS
## For loops will iterate over an iterable and run a block of code

## Syntax example

## for <placeholder> in <iteratable>:
    #Indentation code stuff in this block
        #more code indentation and stuff in this block
#:

## note: the block of code exist after the : (colon)
## it is the lines of code that ARE INDEDNTED
## and it stops when the indentation stops

# iteratables are: list, ranges and dictionaries.... and also strings
import time

wish_list = ["rc car","cheese","cheerleaders","white shirts", "sugar laces","reeses pieces"]

# counter = 1
# for item in wish_list:
#     print(counter, "-", item)
#     counter += 1
#     time.sleep(1.2)

## the above code will look at the list, print the item then move onto the next item in the list and print it.


list_data = [["rc car", "cheerleaders", "white shirts", "audi"], ["sugar laces", "reeses pieces", "oil", "cream"]]
for data in list_data:
    print(data)
    counter = 1
    for num in data:
        print(counter,"-",num)
        counter += 1

