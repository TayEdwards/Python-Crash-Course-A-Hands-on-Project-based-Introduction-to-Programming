ten_Cubes = []

for value in range(1, 11):
    ten_Cubes.append(value**3)
    print(ten_Cubes)

for first in ten_Cubes[0:3]:
    print(f'\n The first three items in the list are {first}')

for middle in ten_Cubes[3:7]:
    print(f'\n The middle three items in the list are {middle}')

for last in ten_Cubes[-3:]:
    print(f'\n The last three items in the list are {last}')

