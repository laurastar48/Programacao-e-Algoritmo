n = int(input('Digite um numero inteiro positivo: '))

contador = 1
fatorial = 1

if n >= 0:
    while contador <= n:
            fatorial = fatorial * contador
            contador += 1

    print(f'Fatorial = {fatorial}')
else:
    print('Numero invalido.')
  
