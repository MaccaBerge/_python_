score = 0

spørsmål = input('Hva er hovedstaden i Norge?')

if spørsmål == 'Oslo':
    print('Riktig!')
    score += 1
else:
    print('\nFeil!')

print('Du fikk',score,' ut av 1 mulige poeng!')
