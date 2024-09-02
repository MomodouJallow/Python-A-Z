class Car:
    """A simple attempt to represent a car."""
    
    
    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    
    def read_odometer(self):
        """Print a statement showing a car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
            
    def increment_odometer(self, miles):
        """Add given amount to odometer reading."""
        self.odometer_reading += miles
        
        
# Implement inheritance.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    
    def __init__(self, manufacturer, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(manufacturer, model, year)
        
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
