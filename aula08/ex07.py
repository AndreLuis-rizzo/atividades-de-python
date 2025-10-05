valorcompra = float(input('Digite o valor de sua compra R$: '))
   
if valorcompra >200:
    desconto = 0.20
    valordesconto = valorcompra * desconto
    valorfinal = valorcompra - valordesconto
elif  valorcompra >=100:
    desconto = 0.10
    valordesconto = valorcompra * desconto
    valorfinal = valorcompra - valordesconto
else:
    desconto = 0
    valordesconto = valorcompra * desconto
    valorfinal = valorcompra - valordesconto
  

print(f'O valor da compra é de: {valorcompra:.2f} ')
print(f'O valor do desconto  é de: {desconto*100} % = {valordesconto:.2f} ')
print(f'O valor final fiocu: {valorfinal:.2f} ')