# Start with the list you used in names.py, but instead of just
# printing each person’s name, print a message to them. The text of each mes-
# sage should be the same, but each message should be personalized with the
# person’s name.

names = ['adam', 'dembo', 'malick', 'usman', 'seedy']
print(f"How do you do, {names[0].title()}?")
print(f"How do you do, {names[1].title()}?")
print(f"How do you do, {names[2].title()}?")
print(f"How do you do, {names[3].title()}?")
print(f"How do you do, {names[4].title()}?")

print("--------------------------------------------")

# Alternatively with a for-loop
for name in names:
    print(f"How do you do, {name.title()}?")