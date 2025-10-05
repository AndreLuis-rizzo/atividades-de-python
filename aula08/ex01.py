numero = float(input('digite um numero: '))
if (numero %3==0) and (numero %5==0):
    print('multiplos de ambos')
elif numero %3==0:
    print('multiplo de 3')
elif numero %5==0:
    print('multiplo de 5 ')
else:
    print('nao e multiplo nem de 3 e nem de 5 ')

