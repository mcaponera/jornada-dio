# 💻️ Introdução ao Python3

linguagem multiplataforma, com tipagem dinâmica e forte.

### Operadores Aritméticos
Como na matemática a ordem de execução das operações é:
1. Parênteses
2. Expoentes
3. Multiplicações e divisões (da esquerda para a direita)
4. Somas e subtrações (da esquerda para a direita)

**Adição(+) e subtração(-)**
```python
produto1 = 10
produto2 = 20
print(produto1 + produto2)
>>> 30
print(produto1 - produto2)
>>> -10
```
**Multiplicação(*)**
```python
produto1 = 10
produto2 = 20
print(produto1 * produto2)
>>> 200
```

**Divisão(/) e Divisão Inteira(//)**
```python
x = 12
y = 3
print(x / y)
>>> 4.0

x = 12
y = 2
print(x // y)
>>> 2
```
**Exponenciação( **) e Módulo(%)**
```python
x = 2
y = 3
print(x ** y)
>>> 8

x = 10
y = 3
print(x % y)
>>> 2
```

### Operadores de Comparação

**Igualdade(==)**
```python
saldo = 450
saque = 200

print(saldo == saque)
>>> False
```

**Diferença(!=)**
```python
saldo = 450
saque = 200

print(saldo != saque)
>>> True
```

**Diferença(!=)**
```python
saldo = 450
saque = 200

print(saldo != saque)
>>> True
```
**Maior que(>)/Maior ou igual que(>=)**
```python
saldo = 450
saque = 200

print(saldo > saque)
>>> True

print(saldo >= saque)
>>> True
```
**Menor que(<)/Menor ou igual que(<=)**
```python
saldo = 450
saque = 200

print(saldo < saque)
>>> False

print(saldo <= saque)
>>> False
```

### Operadores de Atribuição
Definem ou subsescrevem o valor de uma variável

**Atribuição Simples(=)**
```python
saldo = 500
print(saldo)
>>> 500
```

**Atribuição com Adição(+=)**
```python
saldo = 500
saldo += 200
print(saldo)
>>> 700
```
**Atribuição com Subtração(-=)**
```python
saldo = 500
saldo -= 100
print(saldo)
>>> 400
```
**Atribuição com Multiplicação(*=)**
```python
saldo = 500
saldo *= 2
print(saldo)
>>> 1000
```
**Atribuição com Divisão(/= e //=)**
```python
saldo = 500
saldo /= 5
print(saldo)
>>> 100.0

saldo = 500
saldo //= 5
print(saldo)
>>> 100
```
**Atribuição com Módulo(%=)**
```python
saldo = 500
saldo %= 480
print(saldo)
>>> 20
```
**Atribuição com Exponenciação( **=)**
```python
saldo = 500
saldo **= 2
print(saldo)
>>> 6400
```

### Operadores de Lógicos

Usados em conjunto com os operadores de comparação, formam expressões lógicas. O retorno da operação é sempre um booleano.
**Operador E(and)**
```python
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
>>> False
```
**Operador OU(or)**
```python
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
>>> True
```
**Operador de Negação(not)**
```python
contatos = []

not contatos
>>> True
```
**Parênteses**
```python
saldo = 1000
saque = 250
limite = 200
conta_especial = True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
>>> True
```

### Operadores de Identidade

Compara se 2 objetos ocupam a mesma posição na memória
```python
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
>>> True

curso is not nome_curso
>>> False

saldo is limite
>>> True
```

### Operadores de Associação

Verifica se um objeto está presente em uma sequência e retornam um booleano
```python
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
>>> True

"maça" not in frutas
>>> True

200 in saques
>>> False
```