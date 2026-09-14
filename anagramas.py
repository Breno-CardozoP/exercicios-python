def IsAnagram(x,y):
    contador=0
    for i in x:
        if(len(x)!=0 and len(y)!=0):
            if(y.count(i)==x.count(i)):
                        contador+=1
            else: return False
        else:
            return False
        
        
    if(contador==len(x)):
        return True
    else:
        return False

palavra1=input("insira a primeira palavra: ")
palavra1=palavra1.upper().replace(" ", "")
palavra2=input("insira a segunda palavra: ")
palavra2=palavra2.upper().replace(" ", "")

if IsAnagram(palavra1,palavra2):     
    print("é anagrama")
else:
    print("não é anagrama")


        
