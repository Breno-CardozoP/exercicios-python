date=input("insira sua data de nascimento")
date=date.replace(" ","")
date=date.replace("/","")


def NumberOfLife(dateTemp):
    soma=0
    NumDate=[int(x) for x in dateTemp]
    
    while(len(NumDate)>1):
        for x in NumDate:
            soma+=x
        NumDate=[int(x) for x in str(soma)]
        soma=0  
    return NumDate

print("valor do numero da vida:",NumberOfLife(date))
    