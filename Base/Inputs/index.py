# Capturando informções do usuário:

print("Hello World!")
print("Aqui vamos capturar dados de um usuário: ")

nome = str(input("Qual seu nome?"))

idade = int(input("Qual a sua idade?"))

gosto = str(input("Oque você mais gosta de fazer?"))

print("Usuário cadastrado")
print("Nome: " + nome)

if(idade < 18):
    print("Ele é menor!")
    print("Idade: " + str(idade))
else:
    print("Idade: " + str(idade))

print("Seu gosto favorito é: " + gosto)
#Fim