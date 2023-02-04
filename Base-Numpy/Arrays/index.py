import numpy as np

array10 = np.arange(10)
print(array10) # Printa na tela um array com 10 valores preenchidos pela biblioteca

arrayTest = np.array([1, 2, 3, 4, 5])
print(arrayTest)

print(array10.type())
# Integers / Numbers
print(array.dtype())
# Int64

# -------------------------------------------------------------

dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro',
        'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital',
        'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS',
        'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

print(dados.shape())
# 258 / (3, 8)
print(dados.size())
print
# 5

# -------------------------------------------------------

info_carros = [44410, 5712, 37123, 0, 25757, 2003, 1991, 1990, 2019, 2006]
np.array(info_carros)
np.array(info_carros).reshape((2, 5))

print(info_carros)
# array([[44410, 5712, 37123, 0, 25757], [ 2003, 1991, 1990, 2019, 2006]])

# Digamos agora que queremos alocar mais informações dentro deste array, e assim adicionar mais uma linha:
dados_new = dados.copy()
dados_new.resize((3, 5))
 # E assim geramos uma nova linha, na qual temos os dados usando outro método, copy()


 # -----------------------------------------------------------------------------

## Estatísticas de array Numpy

# **Vamos fazer um exercício de cálculo utilizando o array dos dados... Primeiramente vamos chamálos:**

anos = np.loadtxt(fname="carros-anos.txt", dtype=int)
km = np.loadtxt(fname="carros-km.txt")
valor = np.loadtxt(fname="carros-valor.txt")

dataset = np.column_stack((anos, km, valor))

np.mean(dataset)
print(dataset)

# 48489.14648578811
