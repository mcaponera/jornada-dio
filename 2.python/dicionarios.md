# Dicionários

Conjunto não ordenado de pares chave:valor, sendo as chaves únicas. São construídos por meio do construtor *dict* ou {}.

```python
pessoa = {"nome":"Maria", "idade":28}

pessoa2 = dict(nome="João", idade=31)
```

**Acessando e Reatribuindo Valores**
```python
pessoa["nome"]
#>>> "Maria"
pessoa["nome"] = "Carlos"
#>>> {"nome":"Carlos", "idade":28}
```
**Dicionários Aninhados**
Armazenam qualquer tipo de objeto como valor, desde que a chave seja um objeto imutável como (strings e números).
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"]
#>>> "3443-2121"
```

**Iterando Dicionários**
```python
for chave in contatos:
    print(chave, contatos[chave])

#Versão Pythonista usando o método {}.itens()
for chave, valor in contatos.items():
	print(chave, valor)
#>>> guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
#>>>  giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
#>>>  chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
#>>>  melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766'}
```

## Métodos da classe list

*{}.clear*
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
contatos.clear()
#>>> {}
```
*{}.copy*
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}
```
*{}.fromkeys*

Cria chaves num dicionário seja ele existente ou não. Pode criar chaves com um valor padrão.

```python
dict.fromkeys(["nome", "telefone"])
#>>> {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio")
#>>> {"nome": vazio, "telefone": "vazio"}
```
*{}.get*

Uma forma de acessar valores num dicionário, não retornando KeyError se a chave for ausente.
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.get(chave)
#>>> None
contatos.get("guilherme@gmail.com")
#>>> {"nome": "Guilherme", "telefone": "3333-2221"}
```
*{}.items*

Retorna uma lista de tuplas com os pares chave:valor contidos no dicionário.
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.items()
#>>> dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
```
*{}.keys*

Retorna as chaves contidas no dicionário.
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
contatos.keys()
#>>> dict_keys(['guilherme@gmail.com', 'giovanna@gmail.com', 'chappie@gmail.com', 'melaine@gmail.com'])
```
*{}.pop*
Remove e retorna o valor da chave da chave removida, pode receber um segundo argumento a ser removido.
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.pop("guilherme@gmail.com")
#>>> {'nome': 'Guilherme', 'telefone': '3333-2221'}
contatos.pop("guilherme@gmail.com", {})
#>>> {}
```
*{}.popitem*

Não recebe argumento.
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.popitem()
#>>> ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
contatos.popitem()
#>>> KeyError
```
*{}.setdefault*

Caso a chave já exista ele não altera o resultado, do contrário cria o par.
```python
contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna")
#>>> "Guilherme"
contato
#>>> {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)
contato
#>>> {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
```
*{}.update*

Não recebe argumento.
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos
#>>> {'guilherme@gmail.com': {'nome': 'Gui'}}
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
contatos
#>>> {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
```
*{}.values*
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
contatos.values()
#>>> dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])
```

*in*
Verifica se uma determinada chave existem num dado dicionário.
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

"guilherme@gmail.com" in contatos
#>>> True
"megui@gmail.com" in contatos
#>>> False
"idade" in contatos["guilherme@gmail.com"]
#>>> False
"telefone" in contatos["giovanna@gmail.com"]
#>>> True
```
*del*
```python
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"] 
#>>> {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}
```