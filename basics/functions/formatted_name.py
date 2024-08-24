def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


scientist = get_formatted_name('albert', 'einstein')
print(scientist)

scientist = get_formatted_name('marie', 'curie')
print(scientist)