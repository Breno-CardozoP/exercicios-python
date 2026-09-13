palavra = input("insira a palavra: ")
palavra = palavra.upper().replace(" ", "")
invertido = palavra[::-1]

if len(palavra) == 0:
    print("Você não digitou nada.")
elif palavra == invertido:
    print("É palíndromo!")
else:
    print("Não é palíndromo.")