x = [['', '  +---+', '      |', '      |', '      |', '      |', '      |', '=========', ''], ['', '  +---+', '  |   |', '      |', '      |', '      |', '      |', '=========', ''], ['', '  +---+', '  |   |', '  O   |', '      |', '      |', '      |', '=========', ''], ['', '  +---+', '  |   |', '  O   |', '  |   |', '      |', '      |', '=========', ''], ['', '  +---+', '  |   |', '  O   |', ' /|   |', '      |', '      |', '=========', ''], ['', '  +---+', '  |   |', '  O   |', ' /|\\  |', '      |', '      |', '=========', ''], ['', '  +---+', '  |   |', '  O   |', ' /|\\  |', ' /    |', '      |', '=========', ''], ['', '  +---+', '  |   |', '  O   |', ' /|\\  |', ' / \\  |', '      |', '=========', '']]


for i in x:
    i.remove('')
    i.remove('')

print(x)
    