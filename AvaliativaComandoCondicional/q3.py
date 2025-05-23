import random
numero_sorteado = random.randint(1, 100)
menor_numero = 1
maior_numero = 100
acertos = 0 

print("Adivinhe um numero entre 1 e 100 em 4 tentativas.")
print("Tentativa: 1 de 4")
print("O número está entre", menor_numero, "e", maior_numero)
#Pede o número ao usúario
#Tentativa 1
palpite = int(input("Diga o seu palpite: "))

if palpite == numero_sorteado:
    print("Parabens, voce acertou o numero!")
    acertos = 1
elif palpite < numero_sorteado:
    menor_numero = palpite + 1
else:
    maior_numero = palpite - 1 
# Tentativa 2
if acertos == 0: 
    print("Tentativa: 2 de 4")
    print("O intervalo atual é entre", menor_numero, "e", maior_numero)

    palpite = int(input("Diga o seu palpite: "))

    if palpite == numero_sorteado:
        print("Parabens, voce acertou o numero!")
        acertos = 1
    elif palpite < numero_sorteado:
        menor_numero = palpite + 1
    else:
        maior_numero = palpite - 1 
#Tentativa 3
if acertos == 0:
    print("Tentativa: 3 de 4")
    print("O intervalo atual é entre", menor_numero, "e", maior_numero)

    palpite = int(input("Diga o seu palpite: "))

    if palpite == numero_sorteado:
        print("Parabens, voce acertou o numero!")
        acertos = 1
    elif palpite < numero_sorteado:
        menor_numero = palpite + 1
    else:
        maior_numero = palpite - 1 
#Tentativa 4
if acertos == 0:
    print("Tentativa: 4 de 4")
    print("O intervalo atual é entre", menor_numero, "e", maior_numero)

    palpite = int(input("Diga o seu palpite: "))

    if palpite == numero_sorteado:
        print("Parabens, voce acertou o numero!")
        acertos = 1
    elif palpite < numero_sorteado:
        menor_numero = palpite + 1
    else:
        maior_numero = palpite - 1 
#Caso o usúario não acerte
if acertos == 1:
    print("Fim de jogo.")
else:
    print("Suas tentativas acabaram!")
    print("Voce nao acertou. O numero era:", numero_sorteado)