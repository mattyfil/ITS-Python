
n:float=float(input("inserisci valore  "))
if n<0:
     print("errore")
elif n%1!=0:
     print(f"devi inserire un valore intero positivo")
  
else:
    cont=0
    i=0
    print(f"il valore è positivo ed intero")
    for i in range (10):
        x:float=float(input("inserisci valore  "))
        if x%n==0:
                cont=cont+1
                i+=1
                print(f"{cont}")
        else:
            print("valore ignorato")
            i+=1
            print(f"{cont}")


    
    
                
        


    

   
    



