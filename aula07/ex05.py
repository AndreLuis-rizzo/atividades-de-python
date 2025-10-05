peso = float(input('digite seu peso(kg): '))
altura = float(input('digite sua altura(m): '))

imc = peso/  (altura**2)

if imc <18.5:
    print(f'IMC = {imc:.2f} (abaixo do peso)')
elif imc <=25:
    print(f'IMC = {imc:.2f} (peso normal)')
elif imc <30:
    print(f' IMC = {imc:.2f} (acima do peso)')
else:
    print(f'IMC = {imc:.2f} (obesidade)')

