# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.


def make_shirt(size, message):
    """Display the size and message on a shirt."""
    print(f"\nThe shirt-size is {size} with the message: {message}.")
    
# Positional argument.  
make_shirt('medium', 'Imagination is more important than knowledge.')

# Keyword argument- order doesn't matter.
make_shirt(message = 'Love trumps all', size='large')