favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

# One way to do this is to sort the keys as they’re returned in the for loop.
# You can use the sorted() function to get a copy of the keys in order:
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, Thank you for taking the time to take the poll.")