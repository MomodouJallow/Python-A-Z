# You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# Start with your program from guests.py. 
# Add a print()call to the end of your program informing people that you 
# found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.




guests = ['einstein', 'newton', 'muhammad', 'nanoba']

guests.insert(0, 'ada')
guests.insert(3, 'harry')
guests.append('turing')

print(f"I would like to invite you to dinner, {guests[0].title()}.")
print(f"I would like to invite you to dinner, {guests[1].title()}.")
print(f"I would like to invite you to dinner, {guests[2].title()}.")
print(f"I would like to invite you to dinner, {guests[3].title()}.")
print(f"I would like to invite you to dinner, {guests[4].title()}.")
print(f"I would like to invite you to dinner, {guests[5].title()}.")
print(f"I would like to invite you to dinner, {guests[6].title()}.")

print(f"\nI found a bigger table!")

