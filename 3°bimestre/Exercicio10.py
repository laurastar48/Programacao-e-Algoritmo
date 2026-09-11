senha = int(input('Digite a senha: '))

senhaCorreta = 1234
tentativas = 1
limiteTentativas = 3

while senha != senhaCorreta and tentativas < limiteTentativas:
    print('Senha incorreta. Tente novamente. ')
    senha = int(input('Digite a senha: '))
    tentativas += 1

if senha == senhaCorreta:
    print('Acesso liberado.')

else:
    print('Acesso bloqueado.')
