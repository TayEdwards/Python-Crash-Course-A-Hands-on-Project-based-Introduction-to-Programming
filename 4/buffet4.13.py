# tuples useful to store a set of values that should not be changed through the life of a program.
basic_foods = ('egg roll', 'tofu on rice', 'crispy squid',
               'sweet & sour pork', 'noodles')

for food in basic_foods:
    print(f'{food}')

# try to modify the tuple
# basic_foods[5] = 'dumplings'
# TypeError: 'tuple' object does not support item assignment
print(f'\nRestraunt changed it''s menu')
basic_foods = ('egg role', 'tofu on rice', 'crispy squid',
               'chicken chow mein', 'dumplings')

for updatedFood in basic_foods:
    print(f'{updatedFood}')
