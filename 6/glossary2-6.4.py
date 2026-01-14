pythonKeyWords = {
    'if' : 'Used for conditional logic, executing code only if a condition is true.',
    'for' : 'Iterates over a sequence (like a list or string) to perform actions on each item.',
    'def' : 'Defines a new function, a reusable block of code.',
    'return' : 'Exits a function and sends back a value.',
    'true/false' : 'Boolean values representing truth or falsehood, crucial for conditions'
}

for keyWord, definition in pythonKeyWords.items():
    print(f'--{keyWord}-- {definition} \n')

pythonKeyWords = {
    'items' : 'Return a new view of the dictionary’s items ((key, value) pairs).',
    'values' : 'Return a new view of the dictionary’s values',
    'sorted' : 'Return a new sorted list from the items in iterable.',
    'keys' : 'Return a new view of the dictionary’s keys.',
    'iter' : 'Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).'
}

for keyValue in pythonKeyWords.keys():
    print(f'\n ---{keyValue}---, {pythonKeyWords.values()}')
