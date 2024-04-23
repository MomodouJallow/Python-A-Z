# You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# Start with your program from more_guests.py. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, 
# print message to that person letting them know you’re sorry you 
# can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at 
# the end of your program.

guests = ['einstein', 'newton', 'muhammad', 'nanoba']
print("I can invite only two people for dinner")

popped_guest_1 = guests.pop(0)
print(f"Sorry, {popped_guest_1.title()}, I can't invite you to dinner.")

popped_guest_2 = guests.pop(0)
print(f"Sorry, {popped_guest_2.title()}, I can't invite you to dinner.")

print(f"{guests[0].title()}, you are still invited to dinner.")
print(f"{guests[1].title()}, you are still invited to dinner.")

del guests[0]
del guests[0]

print(guests)


