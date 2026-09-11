print('Digite 10 números:')

contador = 1
positivos = 0
negativos = 0
zeros = 0

while contador <= 10:
    n = int(input(f'{contador}° número: '))

    if n > 0:
        positivos += 1

    elif n < 0:
        negativos += 1

    else:
        zeros += 1

    contador += 1

print(f'A quantidade de números positivos é {positivos}, negativos {negativos} e iguais a zero {zeros}.')
