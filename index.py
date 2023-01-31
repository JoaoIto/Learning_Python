# Importação padrão do Numpy
import Numpy as np;

# Usada a função de busca do arquivo

km = np.loadtxt('./Numpy/data/carros-km.txt')
anos = np.loadtxt('./Numpy/data/carros-anos.txt', dtype = int)

# Operação de quilometragem média e exibição no console:
km_media = km / (2022 - anos)
print(km_media)