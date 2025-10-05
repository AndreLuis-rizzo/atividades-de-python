lado1 = int(input('digite o lado 1: '))
lado2  = int(input('digite o lado 2: '))
lado3 = int(input('digite o lado 3: '))
if lado1 == lado2 == lado3:
    print('equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('isoceles')
else:
    print('escaleno') 