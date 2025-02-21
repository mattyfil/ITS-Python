n:int=int(input("scrivi il numero"))
if n%1==0 and n>0:
    sum=0
    i=1
    for i in range(n):
        sum=sum+(i*i)
        i+=1
        print(f"{sum}")
                
else:
    print(f"errore deve essere positivo")
