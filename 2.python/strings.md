# Manipulando Strings

**Métodos Úteis**
```python
curso = "pYtHon"

print(curso.upper())
>>> "PYTHON"

print(curso.lower())
>>> "python"

print(curso.title())
>>> "Python"


nome = "     Carlos "

print(nome.strip())
>>> "Carlos"

print(nome.lstrip())
>>> "Carlos "

print(nome.rstrip())
>>> "     Carlos "


cidade = "Timbó"

print(cidade.center(10, "#")) #Define o número de carcteres e o caracter
>>> "##Timbó###"
cidade = "Timbó"

print(".".join(cidade))
>>> "T.i.m.b.ó"
```

# Interpolação de Variáveis

**Old style %**
```python
nome = "Maria"
idade = 28
profissão = "Programadora"
linguagem = "Python"

# %s -> strings %d -> inteiros %f -> float
print("Olá sou %s. Tenho %d anos, trabalho como %s e  estou fazendo um curso de %s."% (nome, idade, profissao, linguagem)) 
>>> Olá sou Maria. Tenho 28 anos, trabalho como Programadora e  estou fazendo um curso de Python.
```
**Format**
```python
nome = "Maria"
idade = 28
profissão = "Programadora"
linguagem = "Python"

print("Olá sou {}. Tenho {} anos, trabalho como {} e  estou fazendo um curso de {}.".format(nome, idade, profissao, linguagem)) 
>>> Olá sou Maria. Tenho 28 anos, trabalho como Programadora e  estou fazendo um curso de Python.

print("Olá sou {3}. Tenho {2} anos, trabalho como {1} e  estou fazendo um curso de {0}.".format(linguagem, profissao, idade, nome)) 

print("Olá sou {name}. Tenho {age} anos, trabalho como {profissao} e  estou fazendo um curso de {linguagem}.".format(name=nome, age=idade, profissao=profissao, linguagem=linguagem)) 

#usando dicionário
pessoa = {"nome": "Maria", "idade": 28, "profissao": "Programadora", "linguagem": "Python"}

print("Olá sou {nome}. Tenho {idade} anos, trabalho como {profissao} e  estou fazendo um curso de {linguagem}.".format(**pessoa)) 
>>> Olá sou Maria. Tenho 28 anos, trabalho como Programadora e  estou fazendo um curso de Python.
```
**f-string**
```python
nome = "Maria"
idade = 28
profissao = "Programadora"
linguagem = "Python"

print(f"Olá sou {nome}. Tenho {idade} anos, trabalho como {profissao} e  estou fazendo um curso de {linguagem}.") 
>>> Olá sou Maria. Tenho 28 anos, trabalho como Programadora e  estou fazendo um curso de Python.
```

**Formatar float com f-string**
```python
pi = 3.141592653589

print(f"O valor de pi é {pi:.2f}")

print(f"O valor de pi é {pi:20.2f}")
```

# Fatiamento de string

```python
nome = "Carlota Joaquina Teresa Marcos Caetana Coleta Francisca de Sales Rafaela Vicenta Ferrer Joana Nepomucena Fernanda Josefa Luísa Singorosa Antônia Francisca Bibiana Maria Casilda Rita Januária e Pasquala"

#var[start:stop:step]
print(nome[0])
>>> C
print(nome[:7])
>>> Carlota
print(nome[-8])
>>> P
print(nome[9:])
>>> aquina Teresa Marcos Caetana Coleta Francisca de Sales Rafaela Vicenta Ferrer Joana Nepomucena Fernanda Josefa Luísa Singorosa Antônia Francisca Bibiana Maria Casilda Rita Januária e Pasquala
print(nome[10:16])
>>> aquina
print(nome[10:16:2])
>>> aun
print(nome[:])
>>> Carlota Joaquina Teresa Marcos Caetana Coleta Francisca de Sales Rafaela Vicenta Ferrer Joana Nepomucena Fernanda Josefa Luísa Singorosa Antônia Francisca Bibiana Maria Casilda Rita Januária e Pasquala
# espelhar a string
print(nome[::-1])
>>> alauqsaP e airáunaJ atiR adlisaC airaM anaibiB acsicnarF ainôtnA asorogniS asíuL afesoJ adnanreF anecumopeN anaoJ rerreF atneciV aleafaR selaS ed acsicnarF ateloC anateaC socraM asereT aniuqaoJ atolraC
```
# String múltiplas linhas (triplas)

```python
nome = "Guilherme"
mensagem = f"""Olá sou {nome}.
        E estudo 
    Python"""
print(mensagem)
>>>Olá sou Guilherme.
        E estudo 
    Python
```