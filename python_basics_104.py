# List in Python
## List are ordered by index (aka Arrays or objects in JS)

## Syntax
## Declare list using []
## seperate objects using ,

crazy_x_landlords = ["Sr.Julio","Jane","Marks"]
print(crazy_x_landlords)
print(type(crazy_x_landlords))

## How to access 1 record in the list, the list starts counting at '0'.
print(crazy_x_landlords[0])

## Accessing other locations
print(crazy_x_landlords[-1])
print(crazy_x_landlords[1])

## new list of places to live
places_to_live = ["Spain","Brazil","France","Nigeria","Japan","Chile"]

## reassign an index
places_to_live[2] = "China"
print(places_to_live[2])

## method .append(object)
print(len(places_to_live))
places_to_live.append("LA")
print(len(places_to_live))

## .insert(object) inserts an item at a given position
places_to_live.insert(0,"Germany")

print(places_to_live)

## .pop(object) can be used to remove something from the list in its given position
places_to_live.pop(1)
print(places_to_live)

## List slicing
    ## used to manage lists
    ## prints from index to end of list, so example below prints from 3rd indexed value in list to the end
print(places_to_live[3:])
    ## can also use print from index to the start of the list
print(places_to_live[:3])

## print from specified index to second specified index (inclusive)
print(places_to_live[1:3])

## skip slicing ---> [start:stop:step].
print(places_to_live[2::4])
print(places_to_live)

## Typles
## Immutable list
## syntax
    ## defined using _(object, objct)
mortal_enemies = ("Mario","Sailormoon","mooncake","berry","jerry")
print(mortal_enemies)
print(type(mortal_enemies))

## if you try to reassign it will break

## mortal_enemies[0] = "Goku"
## print(mortal_enemies)

# Example of creating a cool list for end of world
list_of_kit = []

item_1 = input("What is your first item to take?")
list_of_kit.append(item_1)
item_2 = input("What is your first item to take2?")
list_of_kit.append(item_2)
item_3 = input("What is your first item to take3?")
list_of_kit.append(item_3)

print("Hey there", list_of_kit)