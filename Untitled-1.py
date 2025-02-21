set_a={1,2,3,4,5}
set_b={4,5,6,7,8}
print (set_a.difference(set_b))
...
allAges={"Alice":23,"Bob":26}
AlicesAge=allAges["Alice"]
print(AlicesAge)

Bobsage=allAges["Bob"]
print(Bobsage)

allmenu:dict={"pizza":9.00,"pasta":10.50,"salad":6.50,"wine":4.00,"water":2.30}
pastamenu:float=allmenu["pasta"]
winemenu:float=allmenu["wine"]
print(f"pasta: {pastamenu} euro,wine: {winemenu} euro")

allmenu["Tiramisu"]= 7.99
print(allmenu)

allmenu.pop("salad")
print(allmenu)

allmenu["pasta"]= 24
print(allmenu)


