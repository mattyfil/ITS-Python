#
itsmenu:dict={"pizza":9.00,
"pasta":10.50,
"zuppa":7.00,
"hamburger":15.50,
"Cotoletta":10.00,
"salmone":20.20,
"patatine fritte":5.50,
"patate al forno":5.50,
"verdura radioattiva":7.00,
"tiramisu":6.00,
"focaccia con nutella":6.00,
"coco cola":3.50,
"vino":5.00,
"acqua":1.50}
 
 # managgia la professore che fa venire fame alle 19 di sera

ordine:dict={"pizza":10.50,
"salmone":20.20,
"patatine fritte":5.50,
"focaccia con nutella":6.00,
 "coca cola":3.50}


# conto da pagare
totale:float =0.00


totale = totale +ordine["pizza"]
totale+=ordine["salmone"]
totale+= ordine["patatine fritte"]
totale+= ordine["focaccia con nutella"]
totale+= ordine["coca cola"]



print(f"totale da pagare:{totale}$")




