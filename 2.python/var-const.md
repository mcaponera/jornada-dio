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