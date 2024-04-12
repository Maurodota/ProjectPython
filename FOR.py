texto = input("informe um texto: ")
Vogais = "AEIOU"

for letra in texto: 
    if letra.upper() in Vogais:
        print(letra, end="")

print()

for numero in range (0,11):
    print(numero, end=" ")
print ()

# exibindo a tabuada do 5
for tabuada in range (0,51,5):
    print(tabuada, end=" ")
    print()