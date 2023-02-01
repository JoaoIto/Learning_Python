# Temos as seguintes variáveis:

text = 'A quilometragem média do veículo é '
Km = 100000
Ano_atual = 2019
Ano_fabricacao = 1999

# Para se fazer a conversão utilizando as funções:

printscream = text + str( int( Km / (Ano_atual - Ano_fabricacao) ) ) + ' km';

print(printscream)