name:str=str(input("inserisci nome"))
vendite:float=float(input("inserisci valore"))
max_name=name
max=vendite
min_name=name
min=vendite
cont=0
for cont in range(20):
    new_name:str=str(input("inserisci nuovo nome"))
    new_vendite:float=float(input("inserisci valore"))
    if new_vendite>max:
        max_name=new_name
        max=new_vendite
        cont+=1
    else:
        if new_vendite<min:
            min_name=new_name
            min=new_vendite
            cont+=1
        else:
            continue
        print(max,max_name)
        print(min,min_name)