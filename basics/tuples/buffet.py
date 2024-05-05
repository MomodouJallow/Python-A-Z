# A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the change.
# The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

foods = ('pizza', 'pillawo', 'jollof rice', 'onion soup', 'fries')

print("The foods available are:")
for food in foods:
    print(food)
    
# modify the tuple
#foods[1] = 'matoke'  # Error, you can't modify a tuple

# rewrite the tuple
foods = ('pizza', 'matoke', 'spaghetti', 'onion soup', 'fries')

print("\nThe revised menu is:")
for food in foods:
    print(food)

