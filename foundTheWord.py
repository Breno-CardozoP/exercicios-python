word=input("insira a palavra: ")
order=input("insira a ordem de caracteres: ")

contador=0
for x in word :
    if order.find(x)!=-1:
        contador+=1
if contador >= len(word):
    print("yes")
else: print("No")