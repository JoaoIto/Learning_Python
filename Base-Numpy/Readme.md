# Base - Numpy

**Depois de estudar a base da linguagem que aqui temos de python, na pasta /Base, vamos começar a utilizar a biblioteca do Numpy para estudo de código para Data Science!**

## [Numpy](https://numpy.org/)

**O numpy é um dos pacotes mais importantes dentro do python para processamentos numéricos dentro da linguagem, na qual é um dos pacotes de biblioteca mais bem conhecidos da linguagem, amplamente utilizado em projetos científicos de algoritmos, estrutura de dados, árvore binária, e afins.**

Esta é uma biblioteca de python, usada principalmente em ciência de dados, já que é uma ótima biblioteca e bastante performática da linguagem para dados numéricos, entre inteiros simples, ou arrays, matrizes, etc. 

---

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