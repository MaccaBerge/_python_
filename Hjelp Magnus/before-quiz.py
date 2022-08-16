score = 0

spørsmål = input('Hva er hovedstaden i Norge?')

if spørsmål == 'oslo':
    print('Riktig!\n\n>>> ')
    score += 1
else:
    print('Feil!')


print(f'Din poengsum {score}')