menu = """""
Para começarmos, selecione uma das opções abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """""

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu)

    if opcao == "1":
        print("Depósito\n")
        valor = float(input("Digite o valor a ser depositado: \n")) 

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("operação não foi concluida! O valor informado e inválido.")
        
    elif opcao == "2":
        print("Saque\n")
        valor = float(input("Digite o valor a ser Sacado: \n")) 

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor <= saldo and valor <= limite_saque and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        elif valor > saldo:
            print("Operação Falhou! Você não tem saldo suficiente.\n")
        elif valor > limite_saque:
            print("NÃO AUTORIZADO! Você excedeu o Limite de Saque Diário!\n")
        elif numero_saques >= LIMITE_SAQUES:
            print("NÃO AUTORIZADO! Você excedeu o número de Saques diários permitidos!\n")

    
    elif opcao == "3":
        print("\n============ EXTRATO ============")
        print("Não form realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================")
            
    elif opcao == "0":
        print ("\nO processo foi concluído. Agradecemos pela preferência.")
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
