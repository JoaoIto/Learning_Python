# Estruturas 

## Estruturas de repetição:

Estruturas de repetição
Estruturas ou laços de repetição são capazes de repetir um mesmo bloco de comandos quantas vezes forem definidas.

Se precisamos coletar duas notas e retornar a média de 100 alunos, podemos colocar um bloco dentro de uma estrutura de repetição e pedir para executá-la 100 vezes.

**Com isso, evitamos a criação de um código gigantesco!**

- Exemplo de código:

```py
nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))

print(f'Média: {(nota_1+nota_2)/2}')

nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))

print(f'Média: {(nota_1+nota_2)/2}')

nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))

print(f'Média: {(nota_1+nota_2)/2}')
```

**Este código é inviável!** E se tivermos mais 50, 100, 10000 alunos para serem coletados? Estaríamos em repetição de código infinito, e assim precisamos entender como funciona a lista de repetição, e como ela ajuda nessa situação.

- Exemplo de código a ser feito:

```py
# Definir o número de alunos
num_alunos = 5

# Criar um array vazio para armazenar as notas
notas = []

# Perguntar as notas de cada aluno usando um loop for
for i in range(num_alunos):
    nota = float(input(f'Digite a nota do aluno {i+1}: '))
    notas.append(nota)

# Calcular a média das notas
media = sum(notas) / len(notas)

# Exibir a média na tela
print(f'A média das notas é {media:.2f}.')

```

---

## Estruturas condicionais combinadas:

Agora iremos melhoras este código a partir também da lista de repetição, vamos ao código:

Neste trecho iremos utilizar para avaliar a nota de vários alunos diferentes, e ainda sim, depois conseguir reproduzir na ***lista de repetição*** **a captura da informações desses alunos**, e depois uma ***conficional***, **para dizer se esses alunos foram aprovados ou não**!
- Código:

```py
# Criar array com os nomes dos alunos
alunos = ["Joao", "Lucas", "Emily", "Enzo"]

# Criar um array vazio para armazenar as notas
notas = []

# Perguntar as notas de cada aluno usando um loop for
for i in range(len(alunos)):
    nota = float(input(f'Digite a nota de {alunos[i]}: '))
    notas.append(nota)

# Calcular a média das notas
media = sum(notas) / len(notas)

# Verificar se a média é maior que 7 e exibir mensagem correspondente
if media >= 7:
    print(f'A média das notas é {media:.2f}. Aprovado.')
else:
    print(f'A média das notas é {media:.2f}. Reprovado.')

```

---