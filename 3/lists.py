friends = ['Shane', 'Zac', 'Ezra', 'Matt', 'Elliot', 'Jacob', 'Tondra', 'Byron']

print(friends)
print(friends[6].title())
#accessing last element in the list with -1
print(friends[-1])
#accessing the 3 from the last
print(friends[-3])

#accessing certain parts of a list in a message
message = f"Why hello there good sir {friends[0].title()}"

print(message)