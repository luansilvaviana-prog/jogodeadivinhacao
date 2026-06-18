print(**********************************)
print("bem vindo ao jogo de adivinhação")
print(**********************************)

numero_secreto = 40

chute = input("digite o seu numero: ")
print("você digitou: ", chute )

chuteNumerico = int(chute)

acertou = numero_secreto == chuteNumerico
maior = chuteNumerico > numero_secreto
menor = chuteNumerico < numero_secreto

#se você digitar qualquer numero vou verificar se você acertou ou errou
if(numero_secreto == chuteNumerico):
    print("você acertou!")
else:
    print("você errou!")
#print(end game)
