import Numpy as np;

km = np.loadtxt('./Numpy/data/carros-km.txt')
anos = np.loadtxt('./Numpy/data/carros-anos.txt', dtype = int)

km_media = km / (2022 - anos)
print(km_media)