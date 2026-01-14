fish_list = ['goby fish', 'anabas', 'eel', 'catfish', 'snapper']
print(fish_list)
print('-------------------------------------')
fish_list.append('siamese fighting fish')
print(fish_list)
print('-------------------------------------')

print('current length of the list before deletion' + str(len(fish_list)))

del fish_list[1]
print('-------------------------------------')

print('current length of the list after del ' + str(len(fish_list)))

print('Sorted------------------------------------')

print(sorted(fish_list))

print('Reverse-Sorted----------------------------')

print(sorted(fish_list, reverse=True))

print('List-Sorted-------------------------------')
fish_list.sort()
print(fish_list)
print('List-Resorted-----------------------------')
fish_list.sort(reverse=True)
print(fish_list)
print('POP---------------------------------------')
pop_the_fish = fish_list.pop()
print(pop_the_fish)
print('REMOVE-------------------------------------')
fish_list.remove('goby fish')
print(fish_list)



