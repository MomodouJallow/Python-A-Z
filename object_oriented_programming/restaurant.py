# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.


class Restaurant:
    """A simple model of a restaurant."""
    
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
        
    def describe_restaurant(self):
        """Displays information about the restaurant."""
        print(f"Welcome to {self.restaurant_name.title()}!")
        print(f"At {self.restaurant_name.title()} we offer all kinds of {self.cuisine_type}.")
        
        
    def open_restaurant(self):
        """Simulate the opening of the restaurant."""
        print(f"{self.restaurant_name.title()} is open.")
        
        
        
restaurant = Restaurant("doudou restaurant", "sea-food")

print(f"The name of the restaurant is {restaurant.restaurant_name.title()}.")
print(f"The type of cuisine offered at {restaurant.restaurant_name.title()} is {restaurant.cuisine_type}.\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()