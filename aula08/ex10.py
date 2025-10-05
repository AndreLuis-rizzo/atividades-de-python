produto = float(input('Digite o valor do seu produto: '))
categoria = int(input(' Digite a categoria 1/2/3: '))
if categoria == 1:
    taxa = 0.5
elif categoria == 2:
    taxa = 0.10
elif categoria == 3:
    taxa = 0.20
else:
    print('Categoria invalida')
valortaxa = produto * taxa
valorfinal = produto + valortaxa
print(f'O valor do seu produto com a taxa fica: {valorfinal:.2f} ')