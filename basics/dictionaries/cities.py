# Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.

cities = {
    'banjul':{
        'country':'gambia',
        'population':150_000,
        'fact':'island',
    },
    
    'kampala':{
        'country':'uganda',
        'population':4_000_000,
        'fact':'hilly',
        },
    
    'paris':{
        'country':'france',
        'population':10_000_000,
        'fact':'eiffel tower',
        },
    }

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"
    
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact.title()}")
    