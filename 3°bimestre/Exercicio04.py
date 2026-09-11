n = int(input("Digite um numero: "))
contador = 1
soma = 0
if (n >0):
    while(contador <= n):
        if(contador % 2 == 0):
            soma = soma + contador
        
        contador+=1
    
    print("soma dos pares: ",soma)

else:
    print("Numero inválido, tente outro.")
