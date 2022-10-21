# Estruturas de Dados em Python

## Tuplas

Muito parecida com as listas, a maior diferença é que tuplas são imutáveis. Criamos tuplas usando o construtor ou colocando valores separados por vírgula dentro de parenteses *()*.

Exemplo de construção de listas
```python
frutos = ()

frutas = ("laranja", "maça", "uva",) #a última vírgula é uma boa prática evitando confusão com precedência

letras = tuple("python")

paíse = ("Brasil",)
```

### Acessando Itens da lista

**Acesso Direto**

Os índices iniciam iniciam em *0* e terminam em *-1*
```python
frutas = ("laranja", "maça", "uva",)

frutas[0] 
#>>> laranja
frutas[-1] 
#>>> uva
```
**Fatiamento**

Início, final e passo.

```python
letras = tupla("python")

letras[2:]
#>>> ('t', 'h', 'o', 'n')
print(letras[:3])
#>>> ('p', 'y', 't')
print(letras[1:4:2])
#>>> ('y', 'h')
```

**Iterar Tuplas**

A maneira mais comum é usando o *for*.

```python
carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)
#>>> gol
#>>> celta
#>>> palio
```
**Enumerate**

Identificar o índice do objeto dentro do laço *for*.
```python
carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
#>>> 0: gol
#>>> 1: celta
#>>> 2: palio
```

### Tuplas Aninhada

Representam em geral matrizes bidimencionais
```python
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)
matriz[0] 
#>>> [1, "a", 2]
matriz[0][0]
#>>> 1
matriz[-1][-1]
#>>> "c"
```

## Métodos da classe tuple

*[].count*
```python
carros = ("gol", "celta", "palio")
carros.count("gol")
#>>> 1
```
*[].index*

primeira ocorrencia do objeto
```python
carros = ("gol", "celta", "palio")
carros.index("palio")
#>>> 2
```
```
*len()*

Retorna o tamanho da lista
```python
carros = ["gol", "celta", "palio"]
len(carros)
#>>> 3
```