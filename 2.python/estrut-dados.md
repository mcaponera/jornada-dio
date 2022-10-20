# Estruturas de Dados em Python

## Listas

Listas são obejtos mutáveis que podem armazenar qualquer tipo de objeto de maneira sequencial. Criamos listas usando o construtor ou colocando valores separados por vírgula dentro de colchete *[]*.

Exemplo de construção de listas
```python
frutos =[]

frutas = ["laranja", "maça", "uva"]

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, "São Paulo", True]
```

### Acessando Itens da lista

**Acesso Direto**

Os índices iniciam iniciam em *0* e terminam em *-1*
```python
carro = ["Ferrari", "F8", 4200000, 2020, "São Paulo", True]

carro[0] 
#>>> Ferrari
carro[-1] 
#>>> True
```
**Fatiamento**

Início, final e passo.

```python
letras = list("python")

letras[2:]
#>>> ['t', 'h', 'o', 'n']
print(letras[:3])
#>>> ['p', 'y', 't']
print(letras[1:4:2])
#>>> ['y', 'h']
```

**Iterar Lista**

A maneira mais comum é usando o *for*.

```python
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
#>>> gol
#>>> celta
#>>> palio
```
**Enumerate**

Identificar o índice do objeto dentro do laço *for*.
```python
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
#>>> 0: gol
#>>> 1: celta
#>>> 2: palio
```

### Listas Aninhada

Representam em geral matrizes bidimencionais
```python
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
matriz[0] 
#>>> [1, "a", 2]
matriz[0][0]
#>>> 1
matriz[-1][-1]
#>>> "c"
```

### Compreensão de listas

Oferece uma sintaxe mais curta quando:
1. criar nova lista com base numa lista existente
1. gerar nova lista aplicando alguma função/modificação em uma lista existente

```python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# list comprehension/ list = [retorno iteração]
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numer for numero in numeros if numero % 2 == 0]
```

## Métodos da classe list

*[].append*
```python
carros = ["gol", "celta", "palio"]
carros.append("uno")
#>>> ["gol", "celta", "palio", "uno"]
```
*[].clear*
```python
carros = ["gol", "celta", "palio"]
carros.clear()
#>>> []
```
*[].copy*
```python
carros = ["gol", "celta", "palio"]
copia_carros = carros.copy()
#>>> ["gol", "celta", "palio", "uno"]
```
*[].count*
```python
carros = ["gol", "celta", "palio"]
carros.count("gol")
#>>> 1
```
*[].extend*
```python
carros = ["gol", "celta", "palio"]
carros.extend(["uno", "fiesta"])
#>>> ["gol", "celta", "palio", "uno", "fiesta"]
```
*[].index*

primeira ocorrencia do objeto
```python
carros = ["gol", "celta", "palio"]
carros.index("palio")
#>>> 2
```
*[].pop*

Usando o comportamento de pilha próprio das listas, retira o último elemento da lista. Pode receber um índice
```python
carros = ["gol", "celta", "palio"]
carros.pop()
#>>> "palio"
carros.pop(0)
#>>> "gol"
```
*[].remove*

Recebe como argumento um item da lista a ser removido
```python
carros = ["gol", "celta", "palio"]
carros.remove("celta")
#>>> ['gol', 'palio']
```
*[].reverse*
```python
carros = ["gol", "celta", "palio"]
carros.reverse()
#>>> ['palio', 'celta', 'gol']
```
*[].sort*

Recebe como argumento o reverse(True/False) e key (lambda)
```python
carros = ["gol", "celta", "palio"]
carros.sort()
#>>> ['celta', 'gol', 'palio']
carros.sort(key=lambda x:len(x), reverse=True)
#>>> ['celta', 'palio', 'gol']
```
*len()*

Retorna o tamanho da lista
```python
carros = ["gol", "celta", "palio"]
len(carros)
#>>> 3
```
*sorted()*

Recebe como argumento o iteravel, key(lambda) e reverse(True/False).
```python
carros = ["gol", "celta", "palio"]
carros = ["gol", "celta", "palio", "fiesta", "ka"]
sorted(carros, key=lambda x: len(x))
#>>> ['ka', 'gol', 'celta', 'palio', 'fiesta']
sorted(carros)
#>>> ['celta', 'fiesta', 'gol', 'ka', 'palio']
```