
#1 - Define a dictionary call story1, it should have the followign keys:
        # hero_name, hero_age, start, middle and end
story1 = {'hero_name': "Tommy Wiseau", 'hero_age': 40, 'Start': "It was a cold winter morning", 'Middle': "I was making my way downtown",
     'End': "walking fast, faces pass and I'm home bound"}

#2 - Print the entire dictionary
print(story1)

#3 - Print the type of your dictionary
print((type(story1)))

#4 - Print only the keys
print('hero_name')
print('hero_age')

#4 - print only the values
print(story1.keys())
print(story1.get('hero_name'))
print(story1.get('hero_age'))
print(story1.get('Start'))
print(story1.get('Middle'))
print(story1.get('End'))

#5 - print the individual values using the keys (individually, lots of printi commands)
print(story1.values())
#6 - Now let's reassing the exist key value pairs with user inputs
    # - hero_name, hero_age, hero_power
hero_name =input("What is the name?>")
hero_age = input("How old are they")
hero_power = input("What is their power?")

story1["Hero"] = hero_name

#7 print the story in an organised/formated manor
print(story1["hero_name"], story1["hero_age"])
print(story1['Middle'])
print(story1['End'])
