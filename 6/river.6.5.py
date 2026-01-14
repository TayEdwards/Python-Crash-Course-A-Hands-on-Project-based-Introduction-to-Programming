rivers = {
    'africa' : 'nile',
    'south america' : 'amazon',
    'china' : 'yangzte'
}

for name in rivers.values():
    if name == 'nile':
        print(f'Heard the {name.title()} is nice this time of year')
    elif name == 'amazon':
        print(f'{name} competing for longest river in the world')
    else:
        print(f'{name} is a beautiful river')
    

for riverKey in rivers.keys():
    print(f'The river key is {riverKey}')

for riverValue in rivers.values():
    print(f'The river value is {riverValue}')