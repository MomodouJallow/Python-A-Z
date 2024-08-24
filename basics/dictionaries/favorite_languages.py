favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Use get() to access values
print(favorite_languages.get('zil', 'They did not take the poll.'))

