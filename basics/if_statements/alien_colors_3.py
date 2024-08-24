# Turn your if-else chain from Exercise alien_colors_2.py into an if-elif-
# else chain.
# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

# Version 1
alien_color = 'green'

if alien_color == 'green':
    print('You have just earned 5 points!')
elif alien_color == 'yellow':
    print('You have just earned 10 points!')
elif alien_color == 'red':
    print('You have just earned 15 points')
    

# Version 2
alien_color = 'yellow'

if alien_color == 'green':
    print("You have just earned 5 points!")
elif alien_color == 'yellow':
    print("You have just earned 10 points!")
elif alien_color == 'red':
    print("You have just earned 15 points!")
    

# Version 3
alien_color = 'red'

if alien_color == 'green':
    print("You have just earned 5 points!")
elif alien_color == 'yellow':
    print("You have just earned 10 points!")
elif alien_color == 'red':
    print("You have just earned 15 points!")