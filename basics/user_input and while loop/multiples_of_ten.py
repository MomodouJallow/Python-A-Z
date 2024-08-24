# Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Enter a number, and I'll tell if it's a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten.")
else:
    print(f"\nThe number {number} is not a multiple of ten.")