"""
#entradas
valor dividendo--->int--->Diendo
valor divisor--->int--->Disor
#salidas
valorresultado--->int--> valorrestante
"""
Cont=0
Diendo=int(input("Ingresar valor del Dividendo: "))
Disor=int(input("Ingresar valor del Divisor: "))
if(Disor>0):
  Diendo=Diendo-Disor
else:
  print("no se puede dividir en 0")
while (Diendo>=0):
	Cont=Cont+1
	Diendo=Diendo-Disor
print("La Division es igual a: "+ str(Cont))