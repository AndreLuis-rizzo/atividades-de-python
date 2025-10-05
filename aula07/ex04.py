valor = float(input('Digite o valor da compra : '))
if valor >100:
   valorfinal =  valor * 0.90
   valortotal = valor - valorfinal
else:
   valorfinal = valor
   

print(f'O valor final  da compra R$: {valorfinal:.2f} ')
