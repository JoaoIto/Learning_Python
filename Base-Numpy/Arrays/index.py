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
