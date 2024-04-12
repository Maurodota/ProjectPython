# Sistema de Liberação para maior idade.

MAIOR_IDADE = 18
idade = int(input("Informe sua idade: "))

status = "OK" if idade >= MAIOR_IDADE else "Não"
print (f"{status} atende aos requisitos")
