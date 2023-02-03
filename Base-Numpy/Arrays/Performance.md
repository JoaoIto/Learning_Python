# Arrays no Numpy [...]

**O numpy tem uma base de dados numéricos, um objeto array multidimensional, mais conhecido brutamente como uma matriz, bastante poderoso com desempenho muito bom, em que consta com suas próprias funções, métodos, e recursos a serem utilizados da biblioteca!**

## Performance...

Iremos fazer um teste de performance para que seja entendido dentro da biblioteca o tamanho da velocidade a ser tratada com os números que são criados.

- **O teste de performance é basicamente para se entender a velocidade, portante iremos contar a partir de um array de 1 milhão de números, e iremos medir que ele consegue fazer para multtiplicar todos estes números 1 por 1:**

```python
py_list = list(range(1000000))
np_array = np.arange(1000000)

print(%time for _ in range(100): np_array *= 2)
# CPU times: user 65.2 ms, sys: 0 ns, total: 65.2 ms Wall time: 73.7 ms


print(%time for _ in range(100): py_list = [x * 2 for x in py_list])
# CPU times: user 8.17 s, sys: 1.79 s, total: 9.96 s Wall time: 9.98 s
```

**Aqui temos um tempo muito superior, de aproximadamente 10 segundos. Ou seja, a diferença de desempenho é enorme e representa uma vantagem de se utilizar o Numpy.**
