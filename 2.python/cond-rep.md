# Estruturas Condicionais e de Repetição

**Identação e Blocos**

Mantem o código mais legível e manutenível. E sinaliza início e fim do bloco de código. Usa 4 espaços em branco
```python
def sacar(valor: float):
    saldo = 500
    if saldo >= valor:
        print("valor sacado")
    #fim do bloco if
#fim do bloco método
```

## Condicionais
Desvio de fluxo quando determinadas expressões lógicas são atendidas

**If**

Condicional simples com um único desvio
```python
saldo = 2000
saque = float(input("Informe valor do saque: "))

if saldo >= saque:
    print("Saque realizado!")

if saldo < saque:
    print("Saldo insuficiente!")
```

**If/Else**

Condicional com 2 desvios
```python
saldo = 2000
saque = float(input("Informe valor do saque: "))

if saldo >= saque:
    print("Saque realizado!")

else:
    print("Saldo insuficiente!")
```

**If/Elif/Else**

Condicional com mais de 2 desvios, não existe limete de elifs, mas grandes estruturas condicionais deve ser evitadas.
```python
opcao = int(input("Informe uma opção: [1]Sacar \n[2]Extrato: "))

if opcao == 1:
    valor = = float(input("Informe valor do saque: "))
    # ...
elif opcao == 2:
    print("Exibindo extrato ...")
else:
    sys.exit("Opção inválida")
```
**If Aninhado**

Basta adicionar estruturas if/elif/else dentro do bloco de if/elif/else
```python
if conta_normal:
    if saldo >= saque:
        print("Saque realizado!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
elif conta_universitária:
    if saldo >= saque:
        print("Saque realizado")
    else:
        print("Sem saldo")
```

**If Ternário**

Permite escrever em uma única linha, composto em 3 partes retorno if condição else retorno
```python
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque")
```

## Repetição
Usadas para repetir um trecho de código por um determinado número de vezes, podendo ser conhecido préviamente ou não.

**For**

Percorre um objeto iterável ou quando sabemos o número exato de vezes que o bloco deve ser executado
```python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
```
**For/Else**
```python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("Fim!")
```
**Função Range**

Função *built-in* usada para produzir uma sequencia de inteiros com um início inclusivo e um fim exclusivo. Ex.: range(i,j) i, i+1, i+2, ..., j-1. Recebe 3 argumentos um obrigatório *stop* e dois opcionais *start* e *step* 
```python
for numero in range(10) #apenas argumento obrigatório stop
    print(numero)

>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in range(0, 51, 5) #sendo star=0 stop=51 step=5
    print(numero)

>>> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```
**While**

Usado para repetir quando não sabemos o número exato de vezes que nosso codigo deve ser executado.
```python
opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n: "))

    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo extrato ...")
```

**While/Else**
```python
opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n: "))

    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo extrato ...")
else:
    print("Volte sempre")
```

**Break**

Para a estrutura de repetição, um geral num looping infinito
```python
while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break
    print(numero)
```

**Continue**

Usado para pular um caso específico
```python
for numero in range(100) :

        if numero == 12:
        continue
    print(numero)
```