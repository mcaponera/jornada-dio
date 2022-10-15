# Funções de Entrada e Saída

**Função input**

Recebe um valor do usuário e retorna no formato string
```python
nome = input("Informe seu nome: ")
>>> Informe seu nome: #maria
print(nome)
>>> maria
```
**Função**

Exibe uma saída para o usuário. Possui 1 argumento obrigatório (*varargs*) e 4 opcionais (*sep, end, file, flush*)
```python
nome = "Maria"
sobrenome = "Silva"

print(nome, sobrenome)
>>> Maria Silva

print(nome, sobrenome, end="...\n")
>>> Maria Silva...

print(nome, sobrenome, sep="&")
>>> Maria&Silva
```
## Links Úteis
[Documentação input()](https://docs.python.org/pt-br/3/library/functions.html#input)
[Documentação print()](https://docs.python.org/pt-br/3/library/functions.html#print)