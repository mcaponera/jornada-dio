menu = """
[1] Depósito
[2] Saque
[3] Extrato

[0] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("\nInforme o valor do depósito: "))
                      
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    
        else:
            print("\nOperação falhou! Valor informado é inválido.")
    
    elif opcao == "2":
        valor = float(input("Informe valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nFalhou :( \nSaldo insuficiente.")

        elif excedeu_limite:
            print("\nFalhou :( \nValor do saque maior que o limite permitido.")
        
        elif excedeu_saques:
            print("\nFalhou :( \nLimite diário de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\nFalhou :( \nValor informado é inválido.")

    elif opcao == "3":
        print("\n************  EXTRATO  ************")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("***********************************")

    elif opcao == "0":
        break

    else:
        print("\nFalhou :( \n Selecione novamente uma opção válida.")