# Create a simple dictionary
alien_0 = {'color':'green', 'points':5}

# Access values in a dictionary
print(alien_0['color'])
print(alien_0['points'])


print()

# Add new key-value pairs
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


print()

# Start with an empty dictionary 
alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 15

print(alien_1)


print()

# Modify values in a dictionary
print(f"alien_1 is {alien_1['color']}.")

alien_1['color'] = 'red'
print(f"alien_1 is now {alien_1['color']}.")

print()

# Remove values from a dictionary
print(alien_1)

del alien_1['points']
print(alien_1)