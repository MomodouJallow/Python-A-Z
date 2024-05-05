# Start with your program from pizzas.py. Make a copy of the list of pizzas, 
# and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

pizzas = ['cheese pizza', 'pepperoni pizza', 'margherita pizza', ]
friend_pizzas = pizzas[:]

pizzas.append('meat pizza')
friend_pizzas.append('veggie pizza')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
    
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)