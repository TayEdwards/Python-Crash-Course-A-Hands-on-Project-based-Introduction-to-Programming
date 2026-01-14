favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

people_Take_Poll = {'edward', 'jen', 'james', 'bobby'}

for people_Poll in people_Take_Poll:
    if people_Poll in favorite_languages:
        print(f'Hi there {people_Poll.title()} Please take the poll')
    else:
        print(f'{people_Poll} has taken the poll')