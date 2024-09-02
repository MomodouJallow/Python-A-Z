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
        long_name  = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    
    def read_odometer(self):
        """Print a statement showing a car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
      
    # Change the value of an attribute through a method.  
    def update_odometer(self, mileage):
        """
        Set odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    
    
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
