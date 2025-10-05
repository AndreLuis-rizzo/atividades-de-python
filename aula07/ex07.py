pedido = float(input('Informe o valor do pedido R$: '))
if pedido <50:
    total = pedido + 10
else:
    total = pedido
    print(f'valor total R$: {total:.2f}')
