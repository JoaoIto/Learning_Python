# Operações de array

**Os métodos de array por exemplo em python são muito mais simples do que no próprio JS, já que chamamos os método mais simples. Digamos que queremos fazer uma verificação dentro de um array que um item se encontra, deste modo:**

```python
Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

 # Verificação dentro do array:

'Rodas de liga' in Acessorios

# Resultado: True

'Rodas de liga' not in Acessorios

# Resultado: False
```

**E assim está pronta a verificação dentro da lista**:

Quando ainda queremos Contatenar um array…

---

## Concatenar array

```python
A = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro']
B = ['Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
A + B

['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

# Pedindo a informação de tamanho de array, função len()

len(Acessorios)
# Resultado: 8
```

A concatenação dentro de python aparece de forma simples, na qual temos que somente usamos o sinal de mais, e ainda sim, existe uma função, tipo como temos em length no JS, temos len() em python. E assim conseguimos pedir o tamanho do array que agora esta concatenado.x

---

# Métodos com array

Dentro do JS, temos diversos métodos, e irei escrever aqueles que se diferenciam da linguagem para o python, já que alguns permanecem a mesma função e nomes idênticos, porém temos aqui alguns nomes diferentes…

### Método push() = append()

```python
# Quer puxar um elemento para sua lista:

Acessorios: ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

Acessorios.append('4 x 4')
Acessorios

# Resultado: 
['Ar condicionado', 'Bancos de couro', 'Piloto automático', 'Rodas de liga', 'Sensor crepuscular', 'Sensor de chuva', 'Sensor de estacionamento', 'Travas elétricas', '4 x 4']
```

### Método map() = copy()

**Imagine que desejamos fazer alterações drásticas em uma lista para realizarmos testes, mas ainda mantendo o conteúdo da original. O método `copy()`pode ser usado para fazer uma cópia de uma lista.**

Dentro deste método, ainda sim entendemos que, não podemos simplesmente atribuir novas variáveis quando quisermos que um array seja copiado, dentro do python, esta mesma variável aparece de forma padrão a copiar e espelhar, ou seja, ela só recebe um novo nome da variável denominada, desta forma:

```python
dados = [1, 2, 3, 4]
dados_copia = dados
dados_copia.append(5)

dados_copia
dados

 # Resultado:[1, 2, 3, 4, 5]
 # Resultado:[1, 2, 3, 4, 5]
```

---

### Operador de partição `[:]`

Dentro de um array maior, com várias informações de vários tipos, temos ainda um tipo de operação que faz a parte de partição dessas informações de array. Ele consegue indicação a partir dos argumentos de índice, a partição dessas informações **em diferentes arrays novos!**

```py
# declaração de array de info
lista_info = ["Joao", "Mly", "Enzo", 10, 9, 8, true, true, false]

# partição em diferentes arrays

lista_nomes = lista_info[0:2]
lista_notas = lista_info[3:5]
lista_boolean = lista_info[6:]
```
