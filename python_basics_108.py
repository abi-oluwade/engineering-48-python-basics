# continuation of for loops

dict_data = {
    1: {
        'name': 'Bronson',
        'money': 0.50,
    },
     2:       {
        'name': 'Steve',
        'money': 200.50,
    },
     3:       {
        'name': 'Jake',
        'money': 55.50,
    },
     4:       {
        'name': 'Rick',
        'money': 20.50,
    }, }


for key in dict_data:
    print(key)
    print(dict_data[key])

for key in dict_data:
    print(key, "-->",dict_data[key])

# We want the name of the person, and how much they owe us, after we apply interest (2000%)

for key in dict_data:
    print(dict_data[key]['name'], "owes us:",
          dict_data[key]["money"]*2000 +dict_data[key]['money'])