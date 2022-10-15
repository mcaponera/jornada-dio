# Variáveis e Constantes

**Variáveis**
Valores que podem sofrer alterações durante a execução do programa. É possivel declarar mais de uma variável numa mesma linha basta separa-las por vírgula. O Python cria automaticamente o tipo da variável.

```python
age, name = (23, "Gilherme")
print(f'Meu nome é {name}', tenho {age} anos.)
>>> Meu nome é Guilherme, tenho 23 anos.

# Sobrescrevendo o valor de name
name = 'Giovana'
print(f'Meu nome é {name}', tenho {age} anos.)
>>> Meu nome é Giovana, tenho 23 anos.
```

**Constantes**
Valor que nao sofre alterações ao longo do tempo.
🤚🏽 Não existe tipo constante em Python
A conveção para esses casos é declarar a variável toda em maiúsculas.

```python
ABS_PATH = '/home/user/Documents/'
```

## Boas Práticas

**Snake Case**

valor total
```python
valor_total = 200
```

**Nomes sugestivos**

Declarar variáveis com nomes que sejam autoexplicativos
```python
limite_diario_saque = 1000
```

# Conversão de Tipos
**Inteiro para Float**
```python
preco = 10
print(preco)
>>> 10

preco = float(preco)
print(preco)
>>> 10.0

# O resultado de uma divisão sempre será um float
preco - 10 / 2
print(preco)
>>> 5.0
```

**Float para Inteiro**
```python
preco = 10.30
print(preco)
>>> 10.3
# A conversão em inteiro não é um arredondamento, a casa decial é despresada na conversão
preco = int(preco)
print(preso)
>>> 10

preco = 10
print(preco / 2)
>>> 5.0

print(preco // 2)
>>> 5
```
**Númerico para string**
```python
preco = 10.50
idade = 28
print(str(preco))
>>> 10.5

# concatenando variaveis usando f"{}"
texto =f"idade {idade} preço {preco}
>>> idade 28 preço 10.5
```

**String para Número**
```python
preco = "10.50"
idade = "28"

print(float(preco))
>>> 10.5

print(int(idade))
>>> 28
```

## Erros de conversão
```python
preco = "Python"

print(float(preco))
>>>Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'Python'
```