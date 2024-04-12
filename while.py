opção = -1
# O While vai sempre executar até as contições forem atendidas. (Melhor que usar o FOR para repedição)
while opção != 0:
    opção = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \nDigie uma opção: "))

    if opção == 1:
        print("Sacando...")
    elif opção == 2:
        print("Exibindo o Extrato...")