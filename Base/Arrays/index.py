A = ['Rodas de liga', 'Travas elétricas',
     'Piloto automático', 'Bancos de couro']
B = ['Ar condicionado', 'Sensor de estacionamento',
     'Sensor crepuscular', 'Sensor de chuva']
C = A + B

print(C)
# Resultado: ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
print(C.len())  
# Resultado: 8
print(C[0])
#Resultado : 'Rodas de liga'


# --------------------------------------------------------------------------------------


# Método push() = append()

Acessorios =  ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

Acessorios.append('4 x 4')
print (Acessorios)

# Resultado: ['Ar condicionado', 'Bancos de couro', 'Piloto automático', 'Rodas de liga', 'Sensor crepuscular', 'Sensor de chuva', 'Sensor de estacionamento', 'Travas elétricas', '4 x 4']

# Método map() = copy()

dados = [1, 2, 3, 4]
dados_copia = dados
dados_copia.append(5)

print(dados_copia)
print(dados)

# Resultado:[1, 2, 3, 4, 5]
# Resultado:[1, 2, 3, 4, 5]
