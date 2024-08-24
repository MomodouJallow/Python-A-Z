favorite_cars = {
    'zil':'audi',
    'dembo':'toyota',
    'harry':'bmw',
    'malick':'bmw',
    'seedy':'ferrari',
    'usman':'range rover',
    }

# Loop through key-value pairs
for name, car in favorite_cars.items():
    print(f"{name.title()}'s favorite car is {car.title()}.")
    

friends = ['zil', 'harry']

for name in favorite_cars.keys():
    print(f"Hi {name.title()}")
    
    if name in friends:
        print(f"\t{name.title()}, I see you love {favorite_cars[name].title()}!")
        
if 'bij' not in favorite_cars.keys():
    print("\nBij, what is your favorite car?\n")
    
cars = []   
for car in favorite_cars.values():
    cars.append(car)
    
for car in sorted(set(cars)):
    print(f"{car.title()}: {cars.count(car)}")
    
