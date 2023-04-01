# Inputs

Como também em diversas linguagens, o python tem a função do input como mensagem dentro de uma captura de informações. Podendo ser elas de texto, numéricos, de qualquer forma.

A função input é usada para ler entradas de alguma pessoa usuária no formato de string e retornar esse valor lido. 

- Um exemplo de uso dessa função é o seguinte código:

```py
nome = str(input('Qual é o seu nome? '))
print(nome)
```

Assim que você conseguir rodar a função ele exibirá uma caixa de texto e assim, conseguir digitar e capturar seu nome. Depois disso pedimos para que imprima a variável que usamos para capturar o valor desse input. E assim, **capturado de uma caixa de entrada de texto, temos um *dado*, escrito pelo usuário.**

---

## Testando codando...

O código abaixo faz exemplo do que podemos fazer capturando informações do user:

```py
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
```

### Saída no console: 

<img src="../../.github/consoleInputs.png">