salario = float(input('Digite o valor do seu salario '))

if salario >5000:
    imposto = salario*0.20
   
else:
    imposto = salario*0.10
    

print(f'O valor do seu salario é {salario:.2f} R$ ')
print(f'Imposto: {20 if salario >5000  else 10}% = {imposto:.2f}')
print(f'Salario liquido: {salario - imposto:.2f}')
