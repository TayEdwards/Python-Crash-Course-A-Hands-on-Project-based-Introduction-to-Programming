names = ['Shane', 'Zac', 'Ezra', 'Matt', 'Elliot', 'Jacob', 'Tondra', 'Byron']
names.append('Tay')
for name in names:
    print(name)
print(names[-1])
names.insert(0,'James')
lastest_friend = names.pop()
print(lastest_friend)
pop_Middle = names.pop(3)
print(pop_Middle)
print(len(names))
print(names)
