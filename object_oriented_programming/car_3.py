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
        Set odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
      
    # Increment an attribute's value through a method      
    def increment_odometer(self, miles):
        """Add given amount to the odometer reading."""
        self.odometer_reading += miles
        
        

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()