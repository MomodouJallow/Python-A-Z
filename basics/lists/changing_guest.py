# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# Start with your program from guests.py. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still
# in your list.

guests = ['einstein', 'newton', 'muhammad', 'nanoba']

absent = guests[0]
guests[0] = 'tesla'

print(f"I would like to invite you to dinner, {guests[0].title()}.")
print(f"I would like to invite you to dinner, {guests[1].title()}.")
print(f"I would like to invite you to dinner, {guests[2].title()}.")
print(f"I would like to invite you to dinner, {guests[3].title()}.")

print(f"\n{absent.title()} would not be able to make it.")
