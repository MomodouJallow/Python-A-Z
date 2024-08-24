# Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "\nEnter the toppings you'll like on your pizza:"
prompt += "\nEnter 'quit' to end the program. "

topping = ""
while topping != 'quit':
    topping = input(prompt)
    
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")