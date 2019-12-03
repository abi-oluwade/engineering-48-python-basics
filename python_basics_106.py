# Nested data in list and dictionaries
## a list can have a mixture of strings and ints, as well as list within the list that contain ints.
## to make everything into a comment highlight everything and print forward slash
mix_list =  ["Strings", 98,["more strings", [1,2,"important"]]]
print((mix_list))
print(mix_list[2])
internal_list = mix_list[2]
print(internal_list[1][2])

## //////

embedded_dict = {
    'Status': 'operational',
    'key1': ['car keys','wheels','engine','dog house keys'],
    'staff': {
        'julio man': {
            'name':'julio',
            'last_name': 'man',
            'birth_date': 1980,
            'football club': 'flamengoFC'
        },
        'Julia Venus': {
            'name':'julia',
            'last_name':'venus',
            'birth_date': 1985,
            'football_club':'CubaFC'
        }
    }
}

##Print
### the car keys and dog house keys
### insdie the key 'staff', print the dictionary with the key 'julio cesar'
### from the dictionary

print(embedded_dict['key1'][1], embedded_dict['key1'][-1])
print(embedded_dict['staff']['julio man']['birth_date'])

## so some tips, when trying to return a specific value, keep counting the position in the nest and then in the corresponding nest, so for example, in the print above
## i can index the first and last value in the list using the int,but for julio it is not a list rather you must specify the string in the dictionary.