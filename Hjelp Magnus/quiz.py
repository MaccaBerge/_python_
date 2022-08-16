score = 0

spørsmål = input('Hva er hovedstaden i Norge?\n\n>>> ')

if spørsmål.lower() == 'oslo':
    print('\nRikitg! +1 poeng')
    score += 1
else:
    print('\nFeil! -0,5 poeng')
    score -= 0.5


spørsmål = input('\n\nEr Henrik dum?\n\n>>> ')

if spørsmål.lower() == 'ja':
    print('\nRikitg! +1 poeng')
    score += 1
elif spørsmål.lower() == 'nei':
    print('\nDa er du dum! -0,5 poeng')
else:
    print('\nFeil! -0,5 poeng')
    score -= 0.5

print(f'\nDu fikk {score} ut av 2 mulige poeng!')