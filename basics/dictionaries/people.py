# Start with the program you wrote in person.py.
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.


person_0 = {
    'first':'albert',
    'last':'einstein',
    'city':'new jersey',
    }

person_1 = {
    'first':'marie',
    'last':'curie',
    'city':'paris',
    }

person_2 = {
    'first':'isaac',
    'last':'newton',
    'city':'cambridge'
}


people = [person_0, person_1, person_2]


for person in people:
    first_name = f"{person['first']}"
    last_name = f"{person['last']}"
    city = f"{person['city']}"
    
    print(f"First name: {first_name.title()}")
    print(f"Last name: {last_name.title()}")
    print(f"City: {city.title()}\n")