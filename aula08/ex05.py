idade = int(input('Digite sua idade: '))
grau = input('Digite seu grau de escolaridade: (F/M/S) ')
if idade >=18 and grau == 'S'.lower():
    print('Voce pode se inscrever no concurso. ')
elif idade >=18 and grau == 'M'.lower():
    print('Voce nao possui ensino superior.')
elif idade >=18 and grau == 'F'.lower():
    print('Voce nao possui ensino superior. ')
else:
    print('voce nao possui idade. ')