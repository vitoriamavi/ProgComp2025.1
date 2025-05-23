#Pede o número ao usúario:
numero = int(input("Digite um número de até 4 algarismos: "))
#Divisão utilizada para aplicar cada algarismo em uma variável:
if 0 <= numero < 10000:
    milhar = (numero//1000) % 10
    centena = (numero//100) % 10
    dezena = (numero//10) % 10
    unidade = numero % 10
#Após criar uma variável é somado cada algarismo:
    soma = milhar + centena + dezena + unidade
#Apresenta o resultado.
    print("A soma dos algarismos é:", soma)
#Caso o número não esteja dentro da condição:
else:
    print("Número inválido! digite um número entre 0 e 9999.")