# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.


def make_shirt(size='large', message='I love Python'):
    """Display the size and message on a shirt."""
    print(f"\nThe shirt-size is {size}, with the message: {message}!")
    
    
make_shirt()
make_shirt('medium')
make_shirt('small', 'Hello, world')