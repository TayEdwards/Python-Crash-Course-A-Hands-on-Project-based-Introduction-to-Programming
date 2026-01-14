guess_list = ['sachin', 'tendulkar', 'don bradman']

print(f'yea i thought {guess_list[0].title()} was an okay player')
print(f'well {guess_list[1].title()} was alright i guess')
print(f'hmmm {guess_list[-1].title()} still wasent as good as Tay')
print()
not_a_friend = guess_list.pop(1)
print(f'oooft {not_a_friend.title()} cant make it 2night')
guess_list.insert(1, 'ricky ponting')
print(f'so {guess_list[0].title()} will still make it')
print(f'so will {guess_list[-1].title()} hes a gc')
print(f'but now we going to invite that guy {guess_list[1].title()}')