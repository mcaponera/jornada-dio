# Funções

Consiste em um bloco de código identificado por um nome que pode, ou não, receber parâmetros (sejam valores padrões ou não). Tornam o código mais legível e permitem o reaproveitamento (programação estrururada). Inicia com a palavra reservada *def*.

*Não recebe parâmetro*
```python
def exibir_mensagem():
    print("OLá Mundo!")
```
*Recebe um parâmetro obrigatório*
```python
def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")
```

*Recebe um parâmetro com valor default*
```python
def exibir_mensagem3(nome="Anônimo"):
    print(f"Olá, {nome}!")
```

### Retornando Valores

Retorna um valor, utilizando a palavra reservada return. Toda função Python retorna None por padrão, e pode retornar mais de um valor.

```python
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor
```

### Args e Kwargs

Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.

```python
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sábado, 22 outubro de 2022", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)
```

### Parâmetros especiais

Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados por posição, por posição e nome, ou por nome.

```python
def funcao(pos1, pos2, /, pos_ou_kword, *, kword1, kword2):
    print(modelo, ano, placa, marca, motor, combustivel)
```

### Objetos de Primeira Classe

Podemos atribuir funções a variáveis, passá-las como parâmetro para outras funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionários, etc) ou usar como retorno para uma função (closures).

```python
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar)  # O resultado da operação é = 20

exibir_resultado(10, 10, subtrair)  # O resultado da operação é = 0
```

### Escopo local e escopo global

Dentro do bloco da função o escopo é local, portanto as variáveis devem ser declaradas localmente. Da mesma forma as alterações feitas em objetos imutáveis serão perdidas quando o método terminar.

Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global. 
**Essa NÃO é uma boa prática e deve ser evitada.**
```python
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario
```