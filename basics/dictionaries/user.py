# Looping through key-value pairs of a dictionary
user_o = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }

for key, value in user_o.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")