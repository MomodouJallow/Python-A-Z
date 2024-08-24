# Make several dictionaries, where each dictionary represents a different pet
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet_0 = {
    'animal':'cat',
    'owner':'sarah',
    }

pet_1 = {
    'animal':'dog',
    'owner':'david',
    }

pet_2 = {
    'animal':'parrot',
    'owner':'phil',
    }

pet_3 = {
    'animal':'goldfish',
    'owner':'edward',
    }


pets = [pet_0, pet_1, pet_2, pet_3]


for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner'].title()}\n")