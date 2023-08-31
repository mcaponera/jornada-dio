# Desenvolvimento de um sistema bancário

Deve implementar apenas 3 operações: depósito, saque e extrato.
### Depósito
Deve ser possível depositar valores inteiros positivos, todos os depósitos devem ser armazenados.

### Saque
Deve ser possível realizar no máximo 3 saques diários, com limite de 500,00 por saque. Caso o usuário não tenha saldo, o sistema deve exibir uma mensagem informando. Todos os depósitos devem ser armazenados.

### Extrato
Deve listar todos os depósitos e saques realizados e ao fim o saldo atual da conta. Se não houver movimentação na conta, deve exibir a mensagem: "*Não foram realizadas movimentações.*" Os valores devem ser exibidos no formato: *R$ xxx.xx*.

[Resolução](./desafio_banco.py)

# Otimizando o Sistema Bancário com Funções Python
O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas, refatorando o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo.

[Resolução](./desafio_banco2.py)
