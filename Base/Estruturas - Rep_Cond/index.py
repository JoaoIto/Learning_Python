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
