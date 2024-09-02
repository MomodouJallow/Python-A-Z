class Car:
    """A simple attempt to represent a car."""
    
    
    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    
# Instantiation
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())