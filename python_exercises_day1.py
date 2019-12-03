# declare some strings
example_string1 = "Hello World"
example_string2 = "This is another string which I have declared"
example_string3 = "It is possible to concatenate strings together."
print(example_string2 + " ." + example_string3)

# prompt user for his/her name
# Save it to some variables with good names
user_name_prompt1 = input("Welcome to my coding environment! What is your name?")

# prompt the user for some random number between 0 - 99
# store it in a variable called: user_chosen_num
example_string4 = "Wow that's an awesome number!"
user_chosen_num = int(input("Try putting in a number between 0-99 for me!"))
if user_chosen_num <= 99 or user_cho > 0:
    print(str(user_chosen_num) + "! " + example_string4 )
else:
    print("Are you blind? I said between 0-99!")

# print a nice welcome message using user name
user_name_prompt1 = input("Welcome to my coding environment! What is your name?")
print("Hello there" + "  " + user_name_prompt1 + "  " + "I hope you're read to learn some python today!")

# request the users last_name
user_name_prompt2 = input("I think we should know each other a little better, what is your last name?")

# Print a nice message welcoming the user using their first and last name
print(user_name_prompt1 + " " + user_name_prompt2 + "!" + "Wow that's a really beautiful name, we're really becoming close")

# Ask for the users age
user_age_prompt1 = int(input("Since we are so close, I think it is about time you told me how old you were!"))
user_age_year = int(2019 - user_age_prompt1)

# print a message of the users age and what year they were born in
print(str(user_age_prompt1) + " " + "that means you were born in" + " " + str(user_age_year))

# Compare the users input to the number they chose at the start and compare it