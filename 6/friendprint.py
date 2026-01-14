# dictionary 
favorite_languages = {
    'phil' : 'Python',
      'sarah' : 'c'}
# our friends :)
friends = ['phil', 'sarah']
# get the name from the dict
for name in favorite_languages.keys():
    print(f'Hi {name.title()}.')
    # if our friends are in our friends_list add it to a variable
    # so we may then print the language they enjoy the most
    # So check if names is in friends list
    if name in friends:
        # Current value of the name is the key to our dict
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}!')
