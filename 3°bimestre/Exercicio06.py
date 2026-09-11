n = float(input("Digite um numero entre 0 e 10: "))

soma = 0
quantidade = 0

while n >= 0 and n <= 10:
    soma += n
    quantidade += 1

    n = float(input("Digite outro numero entre 0 e 10: "))

if quantidade > 0:
    media = soma / quantidade
    print(f"Media das notas:", soma / quantidade)
else:
    print("Nenhuma nota valida foi digitada.")
