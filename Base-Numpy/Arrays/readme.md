# Métodos array Numpy
### `arange()`

**Esta primeira função em uma array, constrói um array a partir do valor final indicado, e assim ela consegue criar com determinado tamanho!**

A partir disso, mesmo assim ainda podemos criar um array comum a partir dos comandos de array dentro do parêntese, como argumentos.

```python
import numpy as np

array10 = np.arange(10)
print(array10) # Printa na tela um array com 10 valores preenchidos pela biblioteca

arrayTest = np.array([1, 2, 3, 4, 5])
print(arrayTest)
```

---

### De tipos: `type()` e `dtype()`

**Essas duas funções de array servem para a tipagem de um array construídos, e como já foi falado, o *Numpy* é conhecido por ser uma biblioteca de alta performance numérica nesta construção, portanto, a diferenciação destas duas funções se dá por meio da complexidade.**

```python
print(array10.type())
# Integers / Numbers
print(array.dtype())
# Int64
```

---

### `shape()`

**Esta função é uma que caracteriza o tamanho do array, podendo caracterizar até por meio de matrizes dimensionais, na qual ele mostra tamanho de colunas tanto de linhas!**

```python
dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

print(dados.shape())
# 258 / (3, 8)
```


### `size()`

**Este método retorna o tamanho do array**

```python
dados = [1, 2, 3, 4, 5]
print(dados.size())
#Resposta: 5
```
## Arrays bidimensionais

### `ndarray()`

**Retorna um array contrário, na qual as minhas são invertidas as colunas e vice versa.**

### `reshape()` e `resize()`

**Diria que é um dos métodos mais bem conhecidos, performáticos e úteis dentro da biblioteca, em um array São dois arrays que interferem justamente no tamanho do array.** 

**Sua diferenciação acontece quando o método *`reshape()`* trabalha a partir de apenas alterar a formação da matriz array, seu número de linhas e colunas. Já o método de *`resize()`* acontece que além de conseguir modificar o tamanho, consegue modificar e ainda inserir novos dados a partir do local novo ao ser modificado.**

---

## Estatísticas de array Numpy

**Vamos fazer um exercício de cálculo utilizando o array dos dados... Primeiramente vamos chamálos:**


```python
anos = np.loadtxt(fname = "carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "carros-km.txt")
valor = np.loadtxt(fname = "carros-valor.txt")
```

Usando o atributo shape, conseguiremos verificar que anos é um array de uma dimensão com 258 linhas.

**Queremos agora juntar os nossos arrays, e o Numpy nos oferece uma funcionalidade que permitirá fazermos isso de maneira bem simples: o método column_stack(), que transforma arrays unidimensionais em colunas de um array bidimensional.**

**Criaremos então uma variável dataset para qual atribuiremos a chamada de np.column_stack() recebendo como parâmetro uma tupla contendo os arrays anos, km e valor.**

Como resultado, teremos um único array cujas colunas representam cada um dos arrays anteriores.

```python
dataset = np.column_stack((anos, km, valor))
dataset

#array([[2.0030000e+03, 4.4410000e+04, 8.8078640e+04], [1.9910000e+03, 5.7120000e+03, 1.0616194e+05], [1.9900000e+03, 3.7123000e+04, 7.2832160e+04], [2.0190000e+03, 0.0000000e+00, 1.2454907e+05], [2.0060000e+03, 2.5757000e+04, 9.2612100e+04], ...])

```

**A primeira estatística que calcularemos usando esse dataset é a media, que conseguiremos usando o método *`np.mean().`***

### `np.mean().`


```python
np.mean(dataset)
print(dataset)

#48489.14648578811
```
**Isso acontece porque o Numpy pegou todos os valores do conjunto indiscriminadamente - ou seja, estamos calculando a média de todos os anos, quilometragens e valores juntos, algo que não faz nenhum sentido. Precisaremos informar ao Numpy com que eixo queremos trabalhar, as linhas ou as colunas, algo que é possível por meio do parâmetro axis. Com axis=0, por exemplo, conseguiremos a média das colunas.**

---
