aluguel = float(input('Digite a quantidade de dias que pretende ficar com o carro: '))
diaria = 100
if aluguel >7:
    desconto = 50
    valordiaria = aluguel * diaria
    valorfinal = valordiaria - desconto
    print(f'O valor do aluguel com disconto fica: {valorfinal:.2f} R$ ')
else:
    valordiaria = aluguel * diaria
    print(f'O valor total do aluguel fica: {valordiaria:.2f} R$ ') 