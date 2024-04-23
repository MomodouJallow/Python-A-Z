# Create a list
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles) # Displays the entire list with the square brackets

# Accessing elements in the list
print(bicycles[0])  # Displays the first element in the list - trek

# Using individual elements in the list
message = f"My first bicycle was a {bicycles[1].title()}."

print(message)

print()

# Create a new list
motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

# Modifying an element in the list
motorcyles[0] = 'ducati'  # Changes honda to ducati
print(motorcyles)

print()

# Appending items to a list
fruits = []
fruits.append('orange')
fruits.append('mango')
fruits.append('apple')
fruits.append('melon')

print(fruits)

# Add an item to the end of the list
fruits.append('strawberry')
print(fruits)

# Add an item to any position in the list
fruits.insert(0, 'pineapple')
print(fruits)

print()

# Removing an element from the list using del statement
print(fruits)

del fruits[1]
print(fruits)

# Removing an element from the end of the list using pop() method
print(fruits)

last_item = fruits.pop()
print(fruits)
print(f"\nThe item at the end of the list was {last_item}.")

print()

# Popping items from an position in the list
print(fruits)

fruits.pop(2)
print(fruits)

print()

# Removing an item by value
print(fruits)

fruits.remove('mango')
print(fruits)

print()

# Print a message using a removed item
print(fruits)

favorite_fruit = 'melon'
fruits.remove(favorite_fruit)
print(f"\nMy favorite fruit is {favorite_fruit}.")
