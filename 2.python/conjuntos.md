# Conjuntos em Python

Um set é uma coleção que não possui objetos repetidos.

```python
set([1, 2, 3, 1, 3, 4])
#>>> {1, 2, 3, 4}
set("abacaxi")
#>>> {'i', 'a', 'c', 'x', 'b'} a ordem sempre pode variar
```

**Acessando os dados**

Conjuntos não suportam indexação. É necessário converter em uma lista
```python
numeros = set([1, 2, 3, 1, 3, 4])
numeros = list(numeros)
```
 **Iterando sets**

 Usa a mesma sintaxe das listas e tuplas. Dessa forma é possível também utilizar a função enumerate.

 **Métodos da Classe set**

*{}.union*
 ```python
 conjunto1 = {1, 2}
 conjunto2 = {2,3,4}

conjunto1.union(conjunto2)
#>>> {1, 2, 3, 4}
```
*{}.intersection*
 ```python
 conjunto3 = {1, 2, 3}
 conjunto2 = {2, 3, 4}

conjunto3.intersection(conjunto2)
#>>> {2, 3}
```
*{}.difference*
 ```python
 conjunto3 = {1, 2, 3}
 conjunto2 = {2, 3, 4}

conjunto3.difference(conjunto2)
#>>> {1}
conjunto2.difference(conjunto3)
#>>> {4}
```
*{}.symmetric_difference*
 ```python
 conjunto3 = {1, 2, 3}
 conjunto2 = {2, 3, 4}

conjunto3.symmetric_difference(conjunto2)
#>>> {1, 4}
```
*{}.issubset (subconjunto)*
 ```python
 conjunto3 = {1, 2, 3}
 conjunto2 = {4, 1, 2, 5, 6, 3}

conjunto3.issubset(conjunto2)
#>>> True
conjunto2.issubset(conjunto3)
#>>> False
```
*{}.issuperset*
 ```python
 conjunto3 = {1, 2, 3}
 conjunto2 = {4, 1, 2, 5, 6, 3}

conjunto3.issuperset(conjunto2)
#>>> False
conjunto2.issuperset(conjunto3)
#>>> True
```
*{}.isdisjoint*
 ```python
 conjunto3 = {1, 2, 3, 4, 5}
 conjunto2 = {6, 7, 8, 9}
 conjunto4 = {1, 0}

conjunto3.isdisjoint(conjunto2)
#>>> True
conjunto2.isdisjoint(conjunto3)
#>>> False
```
*{}.add* 
 ```python
 sorteio = {1, 23}

sorteio.add(25)
#>>> {1, 23, 25}
sorteio.add(42)
#>>> {1, 23, 25, 42}
sorteio.add(25)
#>>> {1, 23, 25, 42} não retorna erro se o item já estiver no set
```
*{}.clear* 
 ```python
 sorteio = {1, 23}

sorteio.clear()
#>>> {}
```
*{}.copy* 
 ```python
 sorteio = {1, 23}

sorteio2 = sorteio.copy()
#>>> {1, 23}
```
*{}.discard* 
 ```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
#>>> {2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(45)
#>>> {2, 3, 4, 5, 6, 7, 8, 9, 0} #não retorna erro caso o item não conste no set
```
*{}.remove* 
 ```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.remove(3)
numeros
# {0, 1, 2, 4, 5, 6, 7, 8, 9}
```
*len()*
 ```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
len(numeros)
#>>> 10
```
*in*
 ```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
1 in numeros
#>>> True
20 in numeros
#>>> False
```