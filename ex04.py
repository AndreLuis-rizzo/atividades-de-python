num1 = float(input('Digite um numero: '))
num2 = float(input('digite outro numero: '))
operacao = input('Digite qual operacao deseja: +, - , * ou /: ')

match operacao:
    case '+':
        res = num1 + num2
    case '-':
        res = num1 - num2
    case '*':
        res = num1 * num2
    case '/':
        res = num1 / num2

print(f'O valor da sua opercao é: {res:.2f} ')