# Importação padrão do Numpy
import numpy as np

# Usada a função de busca do arquivo

km = np.loadtxt('./data/carros-km.txt')
anos = np.loadtxt('./data/carros-anos.txt', dtype = int)

# Operação de quilometragem média e exibição no console:
km_media = km / (2022 - anos)
print(km_media)