# Magic Number Game

## When greyed out means the statement is unused
import random

# user_number_prompt = int(input("Give me a number!"))


# if user_number_prompt >= 55:
#     print("Oh no looks like you did not get it right! You were over the number!")
# elif user_number_prompt <= 53:
#     print("Oh no looks like you did not get it right! You were under the value!")
# else:
#     print("You got it right!")

# Weather Clothing Game

user_weather_input = str(input("What does the weather outside look like?"))


if user_weather_input in {"Sunny"}:
    print("Better take your shorts!")
elif user_weather_input in ["Rainy"]:
    print("It's tine to take your jacket!")
elif user_weather_input in {"Stormy"}:
    print("Stay safe and take a big umbrella and coat!")
elif user_weather_input in {"Rainy and Stormy"}:
    print("It is best to stay home!")
else:
    print("I did not quite catch that")