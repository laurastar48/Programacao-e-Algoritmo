'''
    Autor: Gustavo Costa, e Laura alves
    Data: Junho/2026
    Descrição: Lê um número de 1 a 10 e exibe sua tabuada, validando a entrada.
'''
contador = 1

n = int(input(f'Digite um numero de 1 a 10: '))
while n < 1 and n > 10:
  print("Valor invalido, tente outro numero: ")

while (contador <= 10):
  resultado = n * contador
  print(f'{n} X {contador} = {resultado}')
  contador += 1
