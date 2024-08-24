# Choose a color for an alien as you did in alien_colors.py, and
# write an if-else chain.
# If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# Write one version of this program that runs the if block and another that
# runs the else block.


# Version 1
alien_color = 'green'

if alien_color == 'green':
    print("You have just earned 5 points!")  # Executed
else:
    print("You have just earned 10 points!")  # Ignored
    
    
print("---------------------------------------------")  
    
# Version 2
alien_color = 'yellow'

if alien_color == 'green':
    print("You have just earned 5 points!")  # Ignored
else:
    print("You have just earned 10 points!")  # Executed
    
    
