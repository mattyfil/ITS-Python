par_d=0

caso_1:str="()()()"
caso_2:str="(()"
caso_3:str="()))"
caso_4:str="))(("
caso_5:str="(()())"



for i in caso_4:
    if i==")":
        par_d+=1
        print(par_d)
    elif i==")":
        par_d=par_d-1

        if par_d==0:
            print(f"True")
        else:
            print(f"False")


for i in caso_5:
    if i=="(":
        par_d+=1
    elif i==")":
        par_d=par_d-1

if par_d==0:
            print(f"True")
else:
            print(f"False")
    
