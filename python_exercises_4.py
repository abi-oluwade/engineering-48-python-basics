# Magic Number Game

## When greyed out means the statement is unused
import random

guessuesTaken = 0

print("Hello!, what is you name?")
user_name_input = str(input())

# generate the random number, we can use the keyword 'breakpoint()' to debug our code and inspect our variables.
## and stop our code at a specific point in time
number = random.randint(1,1)
print("well" + "  " +user_name_input +"  "+"I am thinking of a number between 1 - 20")

while guessuesTaken < 10:
    print("Take a guess!")
    guess = int(input("Your Guess"))

    guessuesTaken = guessuesTaken + 1

    if guess < number:
        print("Not quite, you were under the value")

    if guess > number:
        print("Not quite, your guess is over the value")

    if guess == number:
        break
if guess == number:
    guessuesTaken = str(guessuesTaken)
    print("Good job" + "  "+ user_name_input + "  " + "you guessed my number in" + " " + guessuesTaken +" "+ "guess(es)!")

if guess != number:
    number = str(number)
    print("Nope. I was thinking of" + number )



# user_number_prompt = int(input("Give me a number!"))
#
#
#
# if user_number_prompt >= number:
#     print("Oh no looks like you did not get it right! You were over the number!")
# elif user_number_prompt <= number:
#     print("Oh no looks like you did not get it right! You were under the value!")
# else:
#     print("You got it right!")

# Weather Clothing Game

# user_weather_input = str(input("What does the weather outside look like?"))


# if user_weather_input in {"Sunny"}:
#     print("Better take your shorts!")
# elif user_weather_input in ["Rainy"]:
#     print("It's tine to take your jacket!")
# elif user_weather_input in {"Stormy"}:
#     print("Stay safe and take a big umbrella and coat!")
# elif user_weather_input in {"Rainy and Stormy"}:
#     print("It is best to stay home!")
# else:
#     print("I did not quite catch that")