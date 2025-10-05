consumo = float(input('Qual foi o valor do seu consumo? '))
if consumo >200:
    taxa = 0.15
else:
    taxa = 0.10
valor_taxa = consumo*taxa
valorfinal = consumo + valor_taxa
print(f'O valor do consumo: {consumo}')
print(f'Valor da gorgeta: {taxa*100} = {valor_taxa:.2f} ')
print(f'Valor final: {valorfinal:.2f} ')
