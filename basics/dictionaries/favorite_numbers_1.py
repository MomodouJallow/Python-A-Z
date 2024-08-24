# Modify your program from favorite_number.py
# so each person can have more than one favorite number. Then print each person’s 
# name along with their favorite numbers.

favorite_numbers = {
    'paul':[5, 7],
    'steve':[10, 7],
    'galleh':[10, 11, 20],
    'chris':[7, 2, 4],
    'messi':[10, 7, 17],
    'zil':[2, 1, 15],
    'seedy':[0, 8,],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are: ")
    
    for number in numbers:
        print(number)