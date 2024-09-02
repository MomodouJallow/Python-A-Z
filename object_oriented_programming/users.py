# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.


class User:
    """A simple attempt to model a user."""
    
    
    def __init__(self, first_name, last_name, username, location, email):
        """Initialize the first_name and last_name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.location = location
        self.email = email
        
        
    def describe_user(self):
        """"Display a summary of the user's information."""
        print("\nHere is a summary of your information:")
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Username: {self.username}")
        print(f"Location: {self.location.title()}")
        print(f"Email address: {self.email}")
        
        
    def greet_user(self):
        """Display a simple personalized message to the user."""
        print(f"\nWelcome, {self.first_name.title()}!")
        
        
        
first_user = User('albert', 'einstein', 'aeinstein', 'princeton', 'albert@gmail.com')
first_user.describe_user()
first_user.greet_user()

second_user = User('marie', 'curie', 'mcurie', 'paris', 'marie@gmail.com')
second_user.describe_user()
second_user.greet_user()

third_user = User('isaac', 'newton', 'inewton', 'cambridge', 'isaac@gmail.com')
third_user.describe_user()
third_user.greet_user()