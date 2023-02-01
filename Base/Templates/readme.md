## Concatenação de string e transformação de tipos

**Dentro do JS, para que consigamos juntar numa frase duas variáveis a partir de uma expressão do console, podemos simplesmente usar uma *template string*:**

```jsx
const nome = "Joao";
const idade = 17;

const frase = `Meu nome é ${nome} e eu tenho idade de ${idade}`;
```

**No python, temos uma diferença de sintaxe, de duas formas, na qual precisamos converter seus tipos, e usar diretamente na frase, usando a função para cada tipo, e format() ao final. Deste modo:**

```python
# Temos as seguintes variáveis:

text = 'A quilometragem média do veículo é '
Km = 100000
Ano_atual = 2019
Ano_fabricacao = 1999

# Para se fazer a conversão utilizando as funções:

text + str( int( Km / (Ano_atual - Ano_fabricacao) ) ) + ' km'
```

**Começamos com o próprio texto base da variável que criamos, e entendemos que isso precisamos transformar tudo em uma string, então para isso usamos a função de `str()`, e logo depois, precisaríamos que assim transformássemos tudo do cálculo de valores de km e anos, para inteiros, e assim utilizamos a função para inteiros, `int()`, muito simplesmente, temos uma *template string* transformada por python.**

---
