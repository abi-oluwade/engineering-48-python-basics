# Lists!

# Define a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _______?????
bjj_belts = ["White","Blue","Purple","Brown","Black"]

# Print the lists and check it's type
print(bjj_belts)
print(type(bjj_belts))

# Print the list's first object
print(bjj_belts[0])

# Print the list's second object
print(bjj_belts[1])

# Print the list's last object
print(bjj_belts[-1])

# Re-define the first item on the list
bjj_belts[0] = "Pink"
print(bjj_belts)

# Re-define another item on the list and print all the list
bjj_belts[1] = "Red"
print(bjj_belts)

# Add an item to the list and print the list
bjj_belts.append("Gold")
print(bjj_belts)

# Remove an item from the list and print the list
bjj_belts.pop(0)
print(bjj_belts)

# Add two items to list and print the list
bjj_belts.insert(0, "Yellow")
bjj_belts.insert(5, "Platinum")
print(bjj_belts)