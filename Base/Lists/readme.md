# Lists

Além das variáveis que já conhecemos (inteiro, float, boolean e string), também existe um tipo de variável capaz de armazenar e agrupar vários itens dentro deles, funcionando como um conjunto de elementos.

Esse tipo de variável é conhecido como ***dado estruturado***, já que é capaz de estruturar e armazenar vários tipos de dados.

Os dados estruturados mais famosos em Pyhton são ***as listas e os dicionários.***

As listas conseguem armazenar vários elementos em ordem. Esses elementos armazenados **podem ser quaisquer tipos de dados - seja inteiros, booleanos, floats ou strings.** Inclusive, conseguem armazenar até mesmo outras listas dentro delas.

Além disso, uma lista não precisa se resumir a apenas um tipo de dado. **É possível armazenar diferentes tipos de dados em mesma lista.**

## Como criar uma lista:

As listas podem ser construídas tal qual uma variável: especifica-se um nome a variável e cria-se uma lista.

A lista deve ser delimitada por colchetes. Dentro desses colchetes, agrupamos os itens separados por vírgulas.

## Métodos

### `items()`

O método basicamente imprime o dicionário na tela:

```py
cadastro = {
    'matricula': 2000168933, 
    'dia_cadastro': 25, 
    'mes_cadastro': 10, 
    'modalidade': 'EAD'
}

# Imprimindo o dicionário:
print(cadastro.items())

# ([('matricula', 2000168933), ('dia_cadastro', 25), ('mes_cadastro', 10), ('modalidade', 'EAD')])
```

### `keys()`

Imprime as chaves dentro do dicionário:

```py
# Retorna uma lista das chaves do dicionário:

print(cadastro.keys())

#dict_keys(['matricula', 'dia_cadastro', 'mes_cadastro', 'modalidade'])
```

### `value()`

Imprime os valores dentro de cada chave:

```py
# Retorna uma lista dos valores dentro das chaves do dicionário:

print(cadastro.values())

#dict_values([2000168933, 25, 10, 'EAD'])
```